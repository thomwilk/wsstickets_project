from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from .models import Ticket

def index(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TicketForm()
    
    tickets = Ticket.objects.all()
    context = {'tickets': tickets, 'form': form}
    return render(request, 'ticketing/index.html', context)

def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket = form.save(commit=False)
            ticket.status = 'Open'
            ticket.save()
            #Send email to admin with ticket details
            mail_subject = 'New ticket submitted'
            message = f"New ticket submitted: {ticket.building.name} Unit {ticket.unit} - {ticket.status}"
            email = EmailMessage(mail_subject, message, to=['thomwilkinson@gmail.com'])
            email.send()
            
            return render(request, 'ticketing/dashboard.html')  # Redirect after POST
    else:
        form = TicketForm()  # An unbound form

    return render(request, 'ticketing/submit_ticket.html', {'form': form})


@login_required
def view_tickets(request):
    tickets = Ticket.objects.exclude(status='Closed')
    context = {'tickets': tickets}
    return render(request, 'ticketing/dashboard.html', context)

@login_required
def all_tickets(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'ticketing/dashboard.html', context)

@login_required
def change_status(request, ticket_id, new_status):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.status = new_status
    ticket.save()
    return redirect('view_tickets')

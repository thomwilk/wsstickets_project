from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from .forms import TicketForm, ReplyForm
from .models import Ticket, Reply
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
            # Send email to admin with ticket details
            mail_subject = 'New ticket submitted'
            context = {
                'building_name': ticket.building.name,
                'unit': ticket.unit,
                'status': ticket.status,
                'description': ticket.description,
                'email': ticket.email,
            }
            html_message = render_to_string('ticketing/email_template.html', context)
            recipient_list = [ticket.email]
            email = EmailMessage(mail_subject, html_message, 'thom.wilkinson@gmail.com', recipient_list)
            email.content_subtype = 'html'
            email.send()
            return redirect('view_tickets')  # Redirect after POST
    else:
        form = TicketForm()  # An unbound form

    return render(request, 'ticketing/submit_ticket.html', {'form': form})

def login_view(request):
    context = {}
    #check credentials and authenticate user
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('view_tickets')
    else:
        context['login_failed'] = True
        return render(request, 'ticketing/login.html', context)

def logout_view(request):
    logout(request)
    context = {'logged_out': True}
    return redirect('/tickets/login/')

def view_tickets(request):
    if not request.user.is_authenticated:
        return redirect('/tickets/login/')
    tickets = Ticket.objects.exclude(status='Closed')
    context = {'tickets': tickets}
    return render(request, 'ticketing/dashboard.html', context)

def all_tickets(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'ticketing/dashboard.html', context)

def change_status(request, ticket_id, new_status):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.status = new_status
    ticket.save()
    return redirect('view_tickets')

def delete_all_tickets(request):
    Ticket.objects.all().delete()
    return redirect('view_tickets')

def reply_ticket(request):
    form = ReplyForm()
    return render(request, 'ticketing/reply_ticket.html', {'form': form})

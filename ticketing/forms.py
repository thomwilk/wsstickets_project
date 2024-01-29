from django import forms
from .models import Ticket, Reply
from captcha.fields import CaptchaField

class TicketForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Ticket
        fields = ['building', 'unit', 'description', 'tenant_name', 'phone_number', 'email', 'entry_permission'] # Include new fields
        labels = {
            'building': 'Building',
            'unit': 'Unit',
            'description': 'Description',
            'tenant_name': 'Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'entry_permission': 'I require 24 hrs. notice to enter my unit.',
        }

class ReplyForm(forms.ModelForm):
    recipient = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea, label='Reply')
    
    class Meta:
        model = Reply
        fields = ['recipient', 'description']
        labels = {
            'recipient': 'Recipient',
            'description': 'Reply',
        }
    
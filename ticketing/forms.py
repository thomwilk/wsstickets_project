from django import forms
from .models import Ticket
from captcha.fields import CaptchaField

class TicketForm(forms.ModelForm):
    captcha = CaptchaField()
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


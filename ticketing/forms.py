from django import forms
from .models import Ticket
from captcha.fields import CaptchaField

class TicketForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Ticket
        fields = ['building', 'unit', 'description', 'phone_number', 'email'] # Include new fields


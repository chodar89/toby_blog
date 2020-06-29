from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'fname',
            'email',
            'subject',
            'message'
        ]
        labels  = {
        'fname': 'First Name',
        }

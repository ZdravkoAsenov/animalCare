from django import forms

from contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['is_answered', 'created_at']

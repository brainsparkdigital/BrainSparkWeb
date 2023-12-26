from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=20, required=False, label='Phone Number')
    address = forms.CharField(max_length=255, required=False, label='Address')
    service_interest = forms.CharField(max_length=255, required=False, label='Service Interest')
    how_found_us = forms.CharField(max_length=255, required=False, label='How did you find us?')
    content = forms.CharField(widget=forms.Textarea, label='Message')

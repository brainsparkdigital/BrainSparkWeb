from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm

def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            service_interest = form.cleaned_data['service_interest']
            how_found_us = form.cleaned_data['how_found_us']
            content = form.cleaned_data['content']

            html = render_to_string('contactform.html', {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'address': address,
                'service_interest': service_interest,
                'how_found_us': how_found_us,
                'content': content,
            })

            send_mail('Contact form submission', 'This is the message', 'noreply@z4hid.com', ['noreply@z4hid.com'], html_message=html)
            return redirect('confirmation')  # Redirect to the confirmation page

    return render(request, 'contact.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')
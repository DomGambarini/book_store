from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse


def contact(request):
    """
    Handle inquiries sent through the website.
    Adapted from an implementation found at Ordinary Coders.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    'djangoproject618@gmail.com',
                    ['djangoproject618@gmail.com']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header detected.')
            messages.success(
                request, 'Your inquiry has been successfully submitted.')
            return redirect('thanks')
        else:
            messages.warning(
                request,
                'Please provide a valid email in the format name@domain.com.'
            )
    else:
        form = ContactForm()

    context = {
        'form': form,
        'on_page': True,
    }

    return render(request, "contact/contact.html", context)


def thanks(request):
    """ Display a thank you message after submitting an inquiry. """
    return render(request, 'contact/thank_you.html')

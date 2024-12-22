from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        print("Post")
        naam = request.POST.get('name')
        email = request.POST.get('from')
        bericht = request.POST.get('message')

        # Validatie
        if not naam or not email or not bericht:
            messages.error(request, "Alle velden zijn verplicht.")
            return render(request, 'contact.html')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Ongeldig e-mailadres.")
            return render(request, 'contact.html')

        # E-mail verzenden
        subject = f"[FRIGOWORLD.BE] - Nieuw bericht van {naam}"
        message = f"Naam: {naam}\nEmail: {email}\n\nBericht:\n{bericht}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['stef.renneboog.1991@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            print("Verstuurd")
            messages.success(request, 'Bericht werd succesvol verstuurd.')
            return render(request, 'contact.html')  # Redirect na succesvol verzenden
        except Exception as e:
            print("Error")
            messages.error(request, f'Er ging iets mis bij het versturen: {e}')

    return render(request, 'contact.html')


def catalogus_overzicht(request):
    return render(request, 'catalogus\catalogus_overzicht.html')
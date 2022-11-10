from django.shortcuts import render
from .models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message sent successfully.')
    return render(request, 'contact.html')

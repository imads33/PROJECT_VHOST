from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from contacts.models import Contacts

# Create your views here.


def register(request):
    # first_name
    # last_name
    # username
    # email
    # password_1
    # reg_date
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/index.html')


def logout(request):
    return render(request, 'pages/index.html')

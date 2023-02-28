import random
from django.shortcuts import render

from generator.forms import PasswordForms


def home(request):
    form = PasswordForms()
    return render(request, 'generator/home.html', context={'form': form})


def get_password(request):

    data = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        data.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        data.extend('0123456789')
    if request.GET.get('special_symbols'):
        data.extend('!?@#$%^&*()-+')

    password = ''
    length = request.GET.get('length')
    for i in range(int(length)):
        password += random.choice(data)

    return render(request, 'generator/password.html', context={'password': password})


def about(request):
    return render(request, 'generator/about.html')

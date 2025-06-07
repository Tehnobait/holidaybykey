from tempfile import template

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def services(request):
    return render(request, 'main/services.html')


def about(request):
    return render(request, 'main/about.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def contact(request):
    return render(request, 'main/contacts.html')

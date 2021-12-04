from django.shortcuts import render
from django.http import HttpResponse


def home_page(response):
    return render(response, 'main/Login.html')

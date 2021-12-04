from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def login(response):
    return redirect('/login')


def home(response):
    return render(response, 'main/MainPage.html')


def register(response):
    if response.method == "POST":
        print("ok")
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        print("nope")
        form = UserCreationForm()
    return render(response, 'main/Register.html', {'form': form})


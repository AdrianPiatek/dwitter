from django.shortcuts import render, redirect
from .forms import CustomUserCreatingForm


def login(response):
    return redirect('/login')


def home(response):
    return render(response, 'main/MainPage.html')


def register(response):
    if response.method == "POST":
        print("ok")
        form = CustomUserCreatingForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        print("nope")
        form = CustomUserCreatingForm()
    return render(response, 'main/Register.html', {'form': form})


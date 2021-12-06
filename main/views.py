from django.shortcuts import render, redirect
from .forms import CustomUserCreatingForm
from django.contrib.auth.models import User
from .models import Post, Comment


def login(response):
    return redirect('login')


def home(response):
    if not response.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.all()
    return render(response, 'main/MainPage.html', {'posts': posts})


def register(response):
    if response.method == "POST":
        form = CustomUserCreatingForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        form = CustomUserCreatingForm()
    return render(response, 'main/Register.html', {'form': form})


def add_post(response):
    return render(response, 'main/addPost.html')


def add_friend(response):
    return render(response, 'main/addFriend.html')


def add_friend(response):
    return render(response, 'main/addFriend.html')

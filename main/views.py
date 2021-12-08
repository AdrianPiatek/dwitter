from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from .models import Post, Comment, Friend
from datetime import datetime


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
    if response.method == 'POST':
        form = PostForm(response.POST, response.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = response.user
            post.add_date = datetime.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(response, 'main/addPost.html', {'form': form})


def add_friend(response):
    if response.method == 'POST':
        form = AddFriendForm(response.POST)
        if form.is_valid():
            whom_username = form.cleaned_data.get('whom')
            user1 = User.objects.get(username=whom_username)
            user2 = response.user
            try:
                Friend.objects.get(whom=user2, who=user1)
                return redirect('add-friend-er')
            except Friend.DoesNotExist:
                friend_rel1 = Friend(who=user1, whom=user2)
                friend_rel2 = Friend(who=user2, whom=user1)
                friend_rel1.save()
                friend_rel2.save()
                return redirect('home')
    form = AddFriendForm
    return render(response, 'main/addFriend.html', {'form': form})

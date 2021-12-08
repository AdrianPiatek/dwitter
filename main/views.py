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
    if not response.user.is_authenticated:
        return redirect('login')
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
    if not response.user.is_authenticated:
        return redirect('login')
    if response.method == 'POST':
        form = AddFriendForm(response.POST)
        if form.is_valid():
            whom_username = form.cleaned_data.get('whom')
            user1 = User.objects.get(username=whom_username)
            user2 = response.user
            try:
                Friend.objects.get(whom=user2, who=user1)
            except Friend.DoesNotExist:
                if user2 == user1:
                    form.add_error('whom', "You is you")
                else:
                    Friend(who=user1, whom=user2).save()
                    Friend(who=user2, whom=user1).save()
                    return redirect('home')
    else:
        form = AddFriendForm()
    return render(response, 'main/addFriend.html', {'form': form})


def add_comment(response, post_id):
    if not response.user.is_authenticated:
        return redirect('login')
    if response.method == 'POST':
        form = AddCommentForm(response.POST)
        if form.is_valid():
            post = Post.objects.filter(pk=post_id)
            if post.exists():
                comment = form.save(commit=False)
                comment.author = response.user
                comment.add_date = datetime.now()
                comment.post = post.get(pk=post_id)
                comment.save()
                return redirect('home')
            else:
                form.add_error('text', "Post doesn't exist")
    else:
        form = AddCommentForm()
    return render(response, 'main/addComment.html', {'form': form})


def show_friends(response):
    return render(response, 'main/showFriends.html')

from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from django.contrib.auth.models import User
from .models import Post, Comment, Friend
from . import logger


def login(response):
    return redirect('login')


def home(response):
    if not response.user.is_authenticated:
        return redirect('login')
    author = User.objects.all().filter(Q(friend__who=response.user) | Q(username=response.user.username))
    posts = Post.objects.all().filter(author__in=author).order_by("-add_date")
    logger.write_log(response.user.username, 'main page visited')
    return render(response, 'main/MainPage.html', {'posts': posts})


def register(response):
    if response.method == "POST":
        form = CustomUserCreatingForm(response.POST)
        if form.is_valid():
            form.save()
            logger.write_log(form.username, 'added user')
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
            post.add_date = timezone.now()
            post.save()
            logger.write_log(response.user.username, 'added post')
            return redirect('home')
    else:
        form = PostForm()
        logger.write_log(response.user.username, 'add post page visited')
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
                    logger.write_log(user1.username, f'{user2.username} added to friends')
                    logger.write_log(user2.username, f'{user1.username} added to friends')
                    return redirect('home')
    else:
        form = AddFriendForm()
        logger.write_log(response.user.username, 'add friend page visited')
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
                comment.add_date = timezone.now()
                comment.post = post.get(pk=post_id)
                comment.save()
                logger.write_log(response.user.username, f'added comment to post id={post_id}')
                return redirect('home')
            else:
                form.add_error('text', "Post doesn't exist")
    else:
        form = AddCommentForm()
        logger.write_log(response.user.username, 'add comment page visited')
    return render(response, 'main/addComment.html', {'form': form})


def show_friends(response):
    if not response.user.is_authenticated:
        return redirect('login')
    friends = Friend.objects.filter(who=response.user)
    logger.write_log(response.user.username, 'show friends page visited')
    return render(response, 'main/showFriends.html', {'friends': friends})


def forgot_password(response):
    return render(response, 'main/forgotPassword.html')

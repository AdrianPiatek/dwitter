from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Post, Comment, Friend


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'}))


class CustomUserCreatingForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'confirm password'}))


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': 'Title'}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['add_date', 'text']


class AddFriendForm(forms.Form):
    whom = forms.CharField(widget=TextInput(attrs={'placeholder': "Friend's nickname"}))

    class Meta:
        fields = ['whom']

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'}))


class CustomUserCreatingForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'confirm password'}))

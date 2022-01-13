from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from .models import Post, Comment, Friend
from django.contrib.auth.models import User


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'}))


class CustomUserCreatingForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'confirm password'}))
    email = forms.CharField(widget=EmailInput(attrs={'class': 'validate', 'placeholder': 'email'}))


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

    def clean(self):
        data = self.cleaned_data.get('whom')
        if not User.objects.filter(username=data).exists():
            self.add_error('whom', "User dose not exist")


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'comment'}))

    class Meta:
        model = Comment
        fields = ['text']

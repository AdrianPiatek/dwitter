from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from .models import Post, Comment, Friend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'}))


class CustomUserCreatingForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'confirm password'}))
    email = forms.CharField(widget=EmailInput(attrs={'class': 'validate', 'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


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


class RecoveryPasswordForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(widget=TextInput(attrs={'placeholder': 'email'}))

    class Meta:
        fields = ['username', 'email']

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if not User.objects.filter(username=username, email=email).exists():
            self.add_error(None, "username or email don't match")


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate', 'placeholder': 'confirm password'}))

    class Meta:
        fields = ['password1', 'password2']

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 == password2:
            self.add_error('password2', 'Password dose not match')

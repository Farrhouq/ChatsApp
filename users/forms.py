from django.contrib.auth.forms import UserCreationForm
from main.models import User
from django.forms import ModelForm
from django import forms

class UserCreateForm(UserCreationForm):

    password1 = forms.CharField(help_text='Create a password', 
    label='Enter Password', 
    widget=forms.PasswordInput())

    password2 = forms.CharField(help_text='', 
    label='Confirm password', 
    widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']


class UserForm(ModelForm):

    email = forms.EmailField()
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']


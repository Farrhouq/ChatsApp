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
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput({
                                 'autofocus': True,
                                 'placeholder': 'Email',
                                 'class': 'form-control'
                             }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput({
                                   'placeholder':
                                   'Password',
                                   'class':
                                   'form-control'
                               }))

    class Meta:
        model = User
        fields = ['email', 'password']


class UserEditForm(ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Email'
        }))
    username = forms.CharField(label='Username',
                            widget=forms.TextInput({
                                'placeholder': 'Username',
                                'class': 'form-control'
                            }))

    class Meta:
        model = User
        fields = ['username', 'email']

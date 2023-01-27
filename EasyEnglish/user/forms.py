from django import forms
from django.forms import TextInput, EmailInput

from .models import User

class LoginForm(forms.Form):
    model = User
    fields = ['username', 'password']

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '  Usuario',  'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '  Contraseña', 'class': 'form-control'}))

class RegisterForm(forms.Form):
    model = User
    fields = ['email', 'username', 'password']

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': '  Correo',  'class': 'form-control'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '  Usuario',  'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '  Contraseña', 'class': 'form-control'}))
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Logeatu zara')
        return redirect('game')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('game')
            else:
                messages.warning(request, 'El correo o la contraseña son incorrectos')

        form=LoginForm()
        return render(request, 'login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password =request.POST.get('password')
        repeatPassword =request.POST.get('repeatPassword')

        if len(password) < 8:
            messages.warning(request, 'La contraseña es muy corta. Debe tener al menos 8 digitos')
            return redirect('register')
        elif password != repeatPassword:
            messages.warning(request, 'Las contraseñas no son iguales')
            return redirect('register')
        else:
            passwordHashed = make_password(password)
            user = User(username=username, email=email, password=passwordHashed)
            try:
                user.save()
                return redirect('login')
            except:
                messages.warning(request, 'El nombre de usuario ya está usado. Elige otro')
                return redirect('register')
    form=RegisterForm()
    return render(request, 'register.html',{'form':form})

def game(request):
    return render(request, 'game.html')


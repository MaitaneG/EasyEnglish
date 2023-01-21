from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
import random
from django.http import JsonResponse

from game.models import Hangman

# Create your views here.
def game(request):
    user=request.user
    return render(request, 'game.html',{'user':user})

def hangman(request):
    return render(request, 'hangman.html')

def logout(request):
    auth_logout(request)
    return redirect('index')

def getHangmanByType(request):
    hangmans = list(Hangman.objects.all().values())
    return JsonResponse(hangmans,safe=False)
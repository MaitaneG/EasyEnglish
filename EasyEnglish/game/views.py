from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

# Create your views here.
def game(request):
    user=request.user
    return render(request, 'game.html',{'user':user})

def hangman(request):
    return render(request, 'hangman.html')

def logout(request):
    auth_logout(request)
    return render(request, 'index.html')
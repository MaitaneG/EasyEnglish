from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout,get_user_model
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import random
from game.models import Hangman

# Create your views here.
@login_required(login_url="/login")
def game(request):
    return render(request, 'game.html')

@login_required(login_url="/login")
def hangman(request):
    return render(request, 'hangman.html')

@login_required(login_url="/login")
def ranking(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'ranking.html',{'users':users})

@login_required(login_url="/login")
def memoryGame(request):
    return render(request, 'memory_game.html')

@login_required(login_url="/login")
def matchVocabulary(request):
    return render(request, 'match_vocabulary.html')

@login_required(login_url="/login")
def getHangmanByType(request):
    types = request.POST.get('types')
    types=types.capitalize()

    hangmans = list(Hangman.objects.filter(types=types).values())
    random.shuffle(hangmans)
    hangman=hangmans.pop()

    return JsonResponse(hangman,safe=False)

@login_required(login_url="/login")
def getCards(request):
    quantity = request.POST.get('quantity')

    words = list(Hangman.objects.all().values())
    random.shuffle(words)

    cardsWords=[]
    for i in range(int(quantity)):
        cardsWords.append(words.pop(i))

    return JsonResponse(cardsWords,safe=False)

def logout(request):
    auth_logout(request)
    return redirect('index')

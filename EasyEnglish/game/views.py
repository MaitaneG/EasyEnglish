import json
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import Window
from django.db.models.functions.window import RowNumber

from django.http import JsonResponse
import random
from vocabulary.models import Term
from user.models import Ranking
from django.db.models import F

# Create your views here.


@login_required(login_url="/login")
def game(request):
    erabiltzaile = Ranking.objects.get(user=request.user)
    return render(request, 'game.html', {'erabiltzaile': erabiltzaile})


@login_required(login_url="/login")
def hangman(request):
    return render(request, 'hangman.html')


@login_required(login_url="/login")
def memoryGame(request):
    return render(request, 'memory_game.html')


@login_required(login_url="/login")
def matchVocabulary(request):
    return render(request, 'match_vocabulary.html')


@login_required(login_url="/login")
def ranking(request):
    erabiltzaileak = Ranking.objects.all().annotate(rank=Window(
    expression=RowNumber(),order_by=F("points").desc())).order_by('-points')
    
    return render(request, 'ranking.html', {'users': erabiltzaileak})


@login_required(login_url="/login")
def getHangmanByType(request):
    types = request.POST.get('types')
    types = types.capitalize()

    hangmans = list(Term.objects.filter(types=types).values())
    random.shuffle(hangmans)
    hangman = hangmans.pop()

    return JsonResponse(hangman, safe=False)


@login_required(login_url="/login")
def getCards(request):
    quantity = request.POST.get('quantity')

    words = list(Term.objects.all().values())
    random.shuffle(words)

    cardsWords = []
    for i in range(int(quantity)):
        cardsWords.append(words.pop(i))

    return JsonResponse(cardsWords, safe=False)


@login_required(login_url="/login")
def plusPoints(request):
    points = request.POST.get('points')
    ranking = Ranking.objects.get(user=request.user)
    ranking.points += int(points)
    ranking.save()
    return JsonResponse("Okay", safe=False)


@login_required(login_url="/login")
def addLearntWords(request):
    data = json.load(request)
    words = data.get('words')

    ranking = Ranking.objects.get(user=request.user)
    terms = Term.objects.all()
    for word in words:
        for term in terms:
            if (term.word == word):
                ranking.learnts.add(term)
    return JsonResponse("Okay", safe=False)


def logout(request):
    auth_logout(request)
    return redirect('index')

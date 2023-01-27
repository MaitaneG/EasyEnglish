from django.shortcuts import render

from game.models import Hangman

# Create your views here.
def vocabulary(request):
    hangman=Hangman.objects.all();
    return render(request, 'vocabulary.html', {'vocabulary':hangman})
from django.shortcuts import render

from game.models import Hangman
from django.http import JsonResponse

# Create your views here.
def vocabulary(request):
    hangman=Hangman.objects.all();
    return render(request, 'vocabulary.html', {'vocabulary':hangman})

def clasifiedVocabulary(request):
    types=request.POST.get("types")
    print(types)
    hangman=list(Hangman.objects.filter(types=types).values());
    return JsonResponse(hangman,safe=False)
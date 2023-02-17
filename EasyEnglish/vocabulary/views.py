from django.shortcuts import render

from vocabulary.models import Term
from django.http import JsonResponse

# Create your views here.
def vocabulary(request):
    term=Term.objects.all()
    term=term.order_by("word")
    return render(request, 'vocabulary.html', {'vocabulary':term})

def clasifiedVocabulary(request):
    types=request.POST.get("types")
    term=Term.objects.filter(types=types);
    term=list(term.order_by("word").values())
    return JsonResponse(term,safe=False)
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Word


class WordsListView(ListView):
    model = Word
    ordering = ['studied']


def test(request):
    if request.method == 'POST':
        request_dict = request.POST.dict()
        for key in request_dict:
            if key == 'csrfmiddlewaretoken':
                continue
            word = Word.objects.get(id=key)
            word.studied = True
            word.save()
    return redirect(reverse('words_list_view'))
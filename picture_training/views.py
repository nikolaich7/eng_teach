from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Word


class WordsListView(ListView):
    model = Word
    ordering = ['studied']

    def post(self, request):
        request_dict = request.POST.dict()
        for key in request_dict:
            if key == 'csrfmiddlewaretoken':
                continue
            if key == 'reset':
                Word.objects.all().update(studied=False)
                break
            word = Word.objects.get(id=key)
            word.studied = True
            word.save()
        return redirect(reverse('words_list_view'))


class WordsDetailView(DetailView):
    model = Word

def test(request):
    return redirect(reverse('words_detail_view', args=[Word.objects.order_by("?").first().pk]))

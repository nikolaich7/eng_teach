from django.views.generic import ListView

from .models import Word

class WordsListView(ListView):
    model = Word

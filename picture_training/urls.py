from django.urls import path
from .views import *

urlpatterns = [
    path('', WordsListView.as_view(), name='words_list_view')
]
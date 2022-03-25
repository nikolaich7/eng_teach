from django.urls import path
from .views import *

urlpatterns = [
    path('test', test, name='test'),
    path('', WordsListView.as_view(), name='words_list_view'),
]
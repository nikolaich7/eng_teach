from django.urls import path
from .views import *

urlpatterns = [
    path('', WordsListView.as_view(), name='words_list_view'),
    path('<int:pk>', WordsDetailView.as_view(), name='words_detail_view'),
    path('test', test, name='test')
]
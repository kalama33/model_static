from django.urls import path
from .views import ItemListView, ItemListView2 

urlpatterns = [
    path('books/', ItemListView.as_view(), name='item-list'),
    path('movies/', ItemListView2.as_view(), name='movies-list'), 
]
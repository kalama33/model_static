from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    
class ItemListView2(ListView):
    model = Item
    template_name = 'item_list2.html'
    context_object_name = 'items'

# Create your views here.

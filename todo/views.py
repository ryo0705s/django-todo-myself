from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse
from django.views.generic import ListView  
# Create your views here.
class TodoList(ListView):
  model = Todo
  context_object_name = "tasks"

# def index(request):
#   return HttpResponse("<h1> hello world</h1>")

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from .models import models, Todo
def index(request):
    latestTodos = Todo.objects.order_by("-id")
    template = loader.get_template("Todo/index.html")
    context = {
        "latestTodos": latestTodos
    }
    return HttpResponse(template.render(context,request))

def about(request, TodoID):
    try:
        todo = Todo.objects.get(pk=TodoID)
    except Todo.DoesNotExist:
        return HttpResponse("<h1>There is no To-Do by this ID</h1>")
    return render(request, "Todo/detail.html", {"todo": todo})

def add(request):
    return render(request, "Todo/newform.html")
def new(request):
    TodoText = request.POST["text"]
    NewTodo = Todo(text=TodoText)
    NewTodo.save()
    return redirect("/todo")
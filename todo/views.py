from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST

from .models import Todo 
from .forms import TodoForms

# Create your views here.
# index function returns index view
def index(request):
    list = Todo.objects.order_by('id')

    form = TodoForms()

    context = {'list' : list , 'form' : form }
    return render(request, 'todo.html',context)
#renders and returns request 
#------------------------------------------#
@require_POST
def addTodo(request):
    form = TodoForms(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')
# 메인 알고리즘
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from todolist.models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request,'todo_list.html', {'todo_list': todos})

def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'start_date': todo.start_date,
        'end_date': todo.end_date,
        'is_completed': todo.is_complete,
        }
    }
    return render(request, 'todo_info.html', context)
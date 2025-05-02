from django.shortcuts import render, get_object_or_404
from todo.models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo_list.html', context)

def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
    }
    return render(request, 'todo_info.html', context)
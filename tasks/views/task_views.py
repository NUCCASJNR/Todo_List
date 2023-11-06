from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms.task import TaskForm
from models.task import Task

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm()
        if form.is_valid:
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            Task.objects.create(user=request.user, description=description)
            return redirect('view_tasks')
    else:
        form = TaskForm()
        return render(request, 'tasks/add_task.html', {'form': form})
    

@login_required
def view_tasks(request):
    tasks = Task.find_all_objs(user=request.user)
    return render(request, 'tasks/view_tasks.html', {'tasks': tasks})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms.task import TaskForm
from tasks.models.task import Task
from tasks.models.user import CustomUser

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Pass request.POST data to the form
        if form.is_valid():  # Check if the form is valid
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            Task.objects.create(user=request.user, title=title, description=description)  # Save the task with user, title, and description
            return redirect('view_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def view_tasks(request):
    tasks = Task.find_all_objs(user_id=request.user.id)
    # user = CustomUser.find_obj(id=tasks.user_id)
    return render(request, 'tasks/view_tasks.html', {'tasks': tasks})

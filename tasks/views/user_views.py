from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from tasks.forms.user import UserForm
from tasks.models.user import User

def register(request):
    """
    Register view
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('view_tasks')
    else:
        form = UserForm()
    return render(request, 'tasks/signup.html', {'form': form})
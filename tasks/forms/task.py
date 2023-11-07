from django import forms
from tasks.models.task import Task

class TaskForm(forms.ModelForm):
    """Task Form"""
    class Meta:
        model = Task
        fields = ['title', 'description']
        
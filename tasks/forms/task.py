from django import forms
from models.task import Task

class TaskForm(forms.ModelForm):
    """Task Form"""
    class Meta:
        model = Task
        fields = ['title', 'description']
        
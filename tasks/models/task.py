from django.db import models
from models.user import User

class Task(models.Model):
    """
    Task class
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length==200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        db_table = 'tasks'
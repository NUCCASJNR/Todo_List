from tasks.models.base_model import BaseModel, models
from tasks.models.user import CustomUser

class Task(BaseModel):
    """
    Task class
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        db_table = 'tasks'

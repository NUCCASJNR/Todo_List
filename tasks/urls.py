from django.urls import path
from tasks.views import user_views, task_views

urlpatterns = [
    path('signup/', user_views.register, name='register'),
    path('add_task/', task_views.add_task, name='add_task'),
    path('view_tasks/', task_views.view_tasks, name='view_tasks')
]
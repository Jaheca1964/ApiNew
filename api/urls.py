from django import path 
from import .views


urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    # Define mas URLs para otras vistas    
]

"""se importa de django urls"""
from django.urls import path
from . import views

urlpatterns = [
    # Define mas URLs para otras vistas
    path('tasks/', views.TaskList.as_view(), name='task-list'),
]

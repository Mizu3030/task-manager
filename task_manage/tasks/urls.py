from django.urls import path
from . import views

urlpatterns = [
    # Task views
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),

    # User registration view
    path('register/', views.register, name='register'),
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Log in and log out
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Register a new user
    path('register/', views.register, name='register'),

    # Tasks
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]

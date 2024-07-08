"""
URL configuration for kanban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todos.views import LoginView, TodoItemView, RegisterUserView, SubtaskView, LogoutView, CustomUserView, GuestLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', TodoItemView.as_view()),
    path('todos/<int:pk>/', TodoItemView.as_view()),
    path('todos/<int:pk>/delete/', TodoItemView.as_view()),
    path('subtasks/', SubtaskView.as_view()),
    path('subtasks/<int:pk>/', SubtaskView.as_view()),
    path('subtasks/<int:pk>/delete/', SubtaskView.as_view()),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('users/', CustomUserView.as_view()),
    path('users/<int:pk>/', CustomUserView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', CustomUserView.as_view(), name='delete_user'),
    path('guest/', GuestLoginView.as_view())
]

from django.contrib import admin
from .models import TodoItem, JoinUser

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(JoinUser)
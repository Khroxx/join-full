from django.contrib import admin
from .models import TodoItem, JoinUser, TodoSubtask

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(JoinUser)
admin.site.register(TodoSubtask)
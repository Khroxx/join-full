from django.contrib import admin
from .models import TodoItem, JoinUser, TodoSubtask
from django.contrib.auth.models import User

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)
    

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(JoinUser)
admin.site.register(TodoSubtask)
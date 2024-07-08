from django.contrib import admin
from .models import TodoItem, TodoSubtask, CustomUser

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)
    

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(TodoSubtask)
admin.site.register(CustomUser)
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import datetime

# Create your models here.

class JoinUser(models.Model):
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128, default="")
    def save(self, *args, **kwargs):
        if self.password: 
            self.password = make_password(self.password)
        super(JoinUser, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}, {self.username}'

class TodoItem(models.Model):
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    status_choices = [
        ('todo', 'To do'),
        ('progress', 'In progress'),
        ('feedback', 'Await feedback'),
        ('done', 'Done'),
    ]
    category_choices = [
        ('userstory', 'User Story'),
        ('technical', 'Technical Task')
    ]
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=50, choices=priority_choices, default='low')
    users = models.ManyToManyField(User, related_name='todo_users', blank=True)
    category = models.CharField(max_length=20, choices=category_choices, default='userstory')
    status = models.CharField(max_length=20, choices=status_choices, default='todo')

    def get_subtasks(self):
        return self.subtasks.all()
    
    def __str__(self):
        return f'({self.id}, {self.status}) {self.title}'
        #return self.title
    
class TodoSubtask(models.Model):
    todo_item = models.ForeignKey(TodoItem, related_name='subtasks', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'
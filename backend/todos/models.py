from django.db import models
import datetime

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    #priority = models.
    #assignedMember = models.
    #category = models.
    #subtask = models.
    #taskId = models.
    #status = models.
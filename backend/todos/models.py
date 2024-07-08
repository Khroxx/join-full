from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
import datetime

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f'({self.email}) {self.username}'


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
    users = models.ManyToManyField(CustomUser, related_name='todo_users', blank=True)
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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
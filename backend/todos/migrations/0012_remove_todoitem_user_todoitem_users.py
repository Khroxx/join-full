# Generated by Django 5.0.6 on 2024-07-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0011_remove_todoitem_subtask_check_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='users',
            field=models.ManyToManyField(related_name='todo_users', to='todos.joinuser'),
        ),
    ]

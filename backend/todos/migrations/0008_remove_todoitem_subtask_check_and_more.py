# Generated by Django 5.0.6 on 2024-07-01 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_rename_user_joinuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='subtask_check',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='subtask_text',
        ),
        migrations.CreateModel(
            name='TodoSubtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('todo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='todos.todoitem')),
            ],
        ),
    ]

from django.db import models
from account.models import User

# Create your models here.

status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-deadline']

class Subtask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    compiled = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']



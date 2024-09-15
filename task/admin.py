from django.contrib import admin
from task.models import Task,Subtask

# Register your models here.
admin.site.register(Task)
admin.site.register(Subtask)

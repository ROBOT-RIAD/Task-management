from rest_framework import serializers
from .models import Task,Subtask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status','deadline','created_by']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields ='__all__'


from django.shortcuts import render
from rest_framework import viewsets
from .models import Task,Subtask
from .serializers import TaskSerializer,SubtaskSerializer
from rest_framework.generics import  RetrieveAPIView

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        created_by_id = self.request.query_params.get("created_by_id", None)
        if created_by_id is not None:
            queryset = queryset.filter(created_by__id=created_by_id)
        return queryset
    
class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        queryset = Subtask.objects.all()
        parent_task_id = self.request.query_params.get("parent_task_id", None) 
        if parent_task_id is not None:
            queryset = queryset.filter(parent_task__id=parent_task_id)
        return queryset


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



    


from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


  # O método get_queryset é sobrescrito para garantir que apenas as tarefas do usuário autenticado sejam retornadas. O método perform_create é sobrescrito para associar a tarefa criada ao usuário autenticado.
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perfom_create(self, serializer):
        serializer.save(user=self.request.user)

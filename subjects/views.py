from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Subject
from .serializers import SubjectSerializer

# Create your views here.

# ViewSet para o modelo Subject, que irá lidar com as operações de CRUD (Create, Read, 
# Update, Delete) para as matérias. Ele utiliza o SubjectSerializer para serializar os
# dados e a permissão de isAuthenticated 
# para garantir que apenas usuários autenticados possam acessar as matérias.]


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
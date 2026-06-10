from django.db import models
from django.conf import settings
from subjects.models import Subject
# Create your models here.

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Baixa'
        MEDIUM = 'medium', 'Média'
        HIGH = 'high', 'Alta'
        
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendente'
        IN_PROGRESS = 'in_progress', 'Em Progresso'
        DONE = 'done', 'Concluída'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)    
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
        

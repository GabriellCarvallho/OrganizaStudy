from django.db import models
from django.conf import settings
from core import settings

# Create your models here.
class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#4A90e2")  # Exemplo: "#RRGGBB"
    icon = models.CharField(max_length=100, blank=True)
    metas_horas_diarias = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']

    
    def __str__(self):
        return self.name
    

from django.db import models
from django.conf import settings


# Create your models here.
class Subject(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=7, default="#4A90e2")  # Exemplo: "#RRGGBB"
    icone = models.CharField(max_length=100, blank=True)
    metas_horas_diarias = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['nome']

    
    def __str__(self):
        return self.nome
    

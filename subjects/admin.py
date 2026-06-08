from django.contrib import admin
from .models import Subject
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'icon', 'metas_horas_diarias', 'criado_em', 'atualizado_em']

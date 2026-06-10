from rest_framework import serializers
from .models import Subject



# campos que serão expostos na API, e os campos de leitura apenas para leitura (geralmente campos de data de criação e atualização) 

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'color', 'icon', 'metas_horas_diarias', 'criado_em', 'atualizado_em']
        read_only_fields = ['criado_em', 'atualizado_em']
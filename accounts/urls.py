from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('disciplinas/', views.subjects_view, name='subjects'),
    path('tarefas/', views.tarefas_view, name='tarefas'),
    path('revisao/', views.revisao_view, name='revisao'),
    path('estatisticas/', views.estatisticas_view, name='estatisticas'),
    path('assistente/', views.assistente_view, name='assistente'),
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),
    path('metas/', views.metas_view, name='metas'),
    path('cronograma/', views.cronograma_view, name='cronograma'),
]
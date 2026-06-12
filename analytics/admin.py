from django.contrib import admin
from .models import StudySession, Streak

@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'started_at', 'duration_minutes']

@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ['user']
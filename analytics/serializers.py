from rest_framework import serializers
from .models import StudySession, Streak


class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = ['id', 'subject', 'started_at', 'ended_at', 'duration_minutes']
        read_only_fields = ['duration_minutes']


class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = ['streakCurrent', 'StreakLongest', 'dateStudyLast']

        
                
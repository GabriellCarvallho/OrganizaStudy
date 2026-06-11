from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import StudySession, Streak
from .serializers import StudySessionSerializer, StreakSerializer


# Create your views here.



class StudySessionViewSet(viewsets.ModelViewSet):
    serializer_class = StudySessionSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return StudySession.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        self.update_streak(serializer.instance)



    def _update_streak(self, user):
        today = timezone.now().date()
        streak, _ = Streak.objects.get_or_create(user=self.request.user)


        if streak.last_study_date == today - timezone.timedelta(days=1):
            return 

        if streak.last_study_date and (today - streak.last_sytudy_date).days == 1:
            streak.streakCurrent += 1
        else:
            streak.streakCurrent = 1

        
        if streak.streakCurrent > streak.StreakLongest:
            streak.StreakLongest = streak.streakCurrent


        
        streak.last_study_date = today

        streak.save()


class StreakView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        sessions = StudySession.objects.filter(user=request.user)
        totalMinutes =sum(s.duration_minutes for s in sessions)
        totalHours = round(totalMinutes / 60, 1)
        streak, _ = Streak.objects.get_or_create(user=request.user)
        return Response({
            'total_minutes': totalMinutes,
            'total_hours': totalHours,
            'current_streak': streak.streakCurrent,
            'longest_streak': streak.StreakLongest,

        })
    

class StatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        sessions = StudySession.objects.filter(user=request.user)
        totalMinutes = sum(s.durationMinutes for s in sessions)
        totalHours = round(totalMinutes / 60, 1)
        return Response({
            'total_hours': totalHours,
            'total_Sessions': sessions.count(),
            'current_streak': Streak.streakCurrent,
            'longest_streak': Streak.StreakLongest,
        })

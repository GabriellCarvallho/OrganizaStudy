from django.db import models
from django.conf import settings
# Create your models here.



class StudySession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='study_sessions')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.SET_NULL, null=True, blank=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(default=0)



    class Meta:
        ordering = ['-started_at']


    def __str__(self):
        return f"{self.user} - {self.started_at.date()}"
    



class Streak(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='streaks')
    streakCurrent = models.PositiveIntegerField(default=0)
    StreakLongest = models.PositiveIntegerField(default=0)
    dateStudyLast = models.DateField(null=True, blank=True)



    def __str__(self):
        return f"{self.user} - {self.streakCurrent} dias"
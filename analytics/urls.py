from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudySessionViewSet, StreakView, StatsView



router = DefaultRouter()
router.register(r'study-sessions', StudySessionViewSet, basename='study-session')



urlpatterns = router.urls + [
    path('streak/', StreakView.as_view(), name='streak'),
    path('stats/', StatsView.as_view(), name='stats'),
]
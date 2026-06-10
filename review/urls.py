from rest_framework.routers import DefaultRouter
from .views import DeckViewSet, FlashcardViewSet


router = DefaultRouter()
router.register(r'decks', DeckViewSet, basename='deck')
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')

urlpatterns = router.urls
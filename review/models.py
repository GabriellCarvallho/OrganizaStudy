from django.db import models
from django.conf import settings
from subjects.models import Subject
# Create your models here.


class Deck(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='decks')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null= True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')
    question = models.TextField()
    answer = models.TextField()
    ease_factor = models.FloatField(default=2.5)
    interval = models.IntegerField(default=1)
    next_review_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question[:50]  # Retorna os primeiros 50 caracteres da pergunta para facilitar a identificação


# Backwards-compatible alias: some files may import `FlashCard` (capital C)
# Keep both names valid to avoid ImportError from older code.
FlashCard = Flashcard
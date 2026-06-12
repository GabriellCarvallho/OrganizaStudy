from django.contrib import admin
from .models import Deck, Flashcard

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'subject', 'created_at']

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['question', 'deck', 'ease_factor', 'interval']
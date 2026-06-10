from rest_framework import serializers
from .models import Deck, Flashcard



class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'question', 'answer', 'ease_factor', 'interval', 'next_review_date', 'created_at']
        read_only_fields = ['ease_factor', 'interval', 'next_review_date', 'created_at']



class DeckSerializer(serializers.ModelSerializer):
    flashcards = FlashcardSerializer(many=True, read_only=True)


    class Meta:
        model = Deck
        fields = ['id', 'name', 'flashcards', 'created_at']
        read_only_fields = ['created_at']


# Backwards-compatible aliases: some modules may import with different capitalization
FlashCardSerializer = FlashcardSerializer
FlashcardSerializer = FlashcardSerializer



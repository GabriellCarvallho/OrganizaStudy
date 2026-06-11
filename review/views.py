from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Deck, Flashcard
from .serializers import DeckSerializer, FlashcardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)
    


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FlashcardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        return Flashcard.objects.filter(deck__user=self.request.user)
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Deck, FlashCard
from .serializers import DeckSerializer, FlashCardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)
    


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FlashcardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashCardSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        return FlashCard.objects.filter(deck__user=self.request.user)
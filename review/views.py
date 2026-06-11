from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Deck, Flashcard
from .serializers import DeckSerializer, FlashcardSerializer
from .sm2 import calculate_sm2

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
    
    @action(detail=True, methods=['post'])
    def review(self, requst, pk=None):
        flashcard = self.get_object()
        quality = request.data.get('quality')

        if quality is None or not (0 <= quality <= 5):
            return Response({'error': 'quality deve estar entre 0 e 5'}, status=status.HTTP_400_BAD_REQUEST)
        
        ease_factor, interval = calculate_sm2(flashcard.ease_factor, flashcard.interval, int(quality))
        flashcard.ease_factor = ease_factor
        flashcard.interval = interval
        flash.card.next_review = timezone.now() + timedelta(days=interval)
        flashcard.save()

        return Response({
            'ease_factor': ease_factor,
            'interval': interval,
            'next_review': flashcard.next_review
        })
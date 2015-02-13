from django.shortcuts import render

# Create your views here.
from models import Player
from serializers import PlayerSerializer
from rest_framework import generics


class PlayersList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

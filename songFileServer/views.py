from django.shortcuts import render
from songFileServer.models import Song, Podcast, Audiobook
from songFileServer.serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from rest_framework import viewsets


# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

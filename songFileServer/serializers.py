from rest_framework import serializers, fields
from songFileServer.models import Song, Podcast, Audiobook
# from django.utils.timezone import now
import datetime

class SongSerializer(serializers.ModelSerializer):
    # uploadedTime = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%SZ'])
    # uploadedTime = fields.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Song
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'

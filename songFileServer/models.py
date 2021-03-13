from django.db import models

# Create your models here.

# class CustomDateTimeField(models.DateTimeField):
#     def value_to_string(self, obj):
#         val = self.value_from_object(obj)
#         if val:
#             val.replace(microsecond=0)
#             return val.isoformat()
#         return ''

class Song(models.Model):
    id=models.IntegerField(primary_key=True)
    songName=models.CharField(max_length=100, blank=False, null=True)
    songDurationSeconds=models.PositiveIntegerField(blank=False, null=True)
    uploadedTime=models.DateTimeField(auto_now_add=True, blank=False, null=True)

class Podcast(models.Model):
    id=models.IntegerField(primary_key=True)
    podcastName=models.CharField(max_length=100, blank=False, null=True)
    podcastDurationSeconds=models.PositiveIntegerField(blank=False, null=True)
    uploadedTime=models.DateTimeField(auto_now_add=True, blank=False, null=True)
    podcastHost=models.CharField(max_length=100, blank=False, null=True)
    podcastParticipants=models.CharField(max_length=100, choices=[], blank=False, null=True)

class Audiobook(models.Model):
    id=models.IntegerField(primary_key=True)
    audiobookTitle=models.CharField(max_length=100, blank=False, null=True)
    titleAuthor=models.CharField(max_length=100, blank=False, null=True)
    audiobookNarrator=models.CharField(max_length=100, blank=False, null=True)
    audiobookDurationSeconds=models.PositiveIntegerField(blank=False, null=True)
    uploadedTime=models.DateTimeField(auto_now_add=True, blank=False, null=True)

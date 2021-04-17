# audio/serializer.py

from .models import Song, Podcast, Audiobook
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = [
            "id", "audio_title", "audio_duration", "date_uploaded"
        ]

class PodcastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Podcast
        fields = [
            "id", "audio_title", "audio_duration", "date_uploaded", "host", "participants"
        ]

class AudiobookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Audiobook
        fields = [
            "id", "audio_title", "audio_duration", "date_uploaded", "author", "narrator"
        ]


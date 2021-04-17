# api/utils.py

from audio.models import Song, Podcast, Audiobook
from audio.serializer import SongSerializer, PodcastSerializer, AudiobookSerializer

from rest_framework.response import Response
from rest_framework import status

AUDIO_FILE_TYPE = ('song', 'podcast', 'audiobook')

class Audio_Model_Serializer():
    
    def __init__(self, audioFileType):
        self.audioFileType = audioFileType

    def audio_model(self):
        """
        Logic for Audio Model Selection
        """

        if self.audioFileType == "song":
            return Song
        elif self.audioFileType == "podcast":
            return Podcast
        elif self.audioFileType == "audiobook":
            return Audiobook
        else:
            return


    def audio_serializer(self):
        """
        Logic for Audio Serializer Selection
        """

        if self.audioFileType == "song":
            return SongSerializer
        elif self.audioFileType == "podcast":
            return PodcastSerializer
        elif self.audioFileType == "audiobook":
            return AudiobookSerializer
        else:
            return

def Bad_Request():
    return Response(
                {"message": "Please specify audioFileID"},
                status=status.HTTP_400_BAD_REQUEST)
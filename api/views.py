# api/views.py
############################
# AUTHOR : PRANEET NIGAM
############################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from django.http import Http404

from .utils import Audio_Model_Serializer, AUDIO_FILE_TYPE, Bad_Request

class AudioView(APIView):

    def get_object(self, audio_ms, fileId):

        audio_model = audio_ms.audio_model()
        try:
            return audio_model.objects.get(pk=fileId)
        except audio_model.DoesNotExist:
            raise Http404
    
    def get(self, request, 
            audioFileType = None, audioFileID = None,  
            format=None, *args, **kwargs):
        
        """
        GET & RETRIEVE REQUEST
        """

        if audioFileType not in AUDIO_FILE_TYPE:
            return Bad_Request()
        
        audio_ms = Audio_Model_Serializer(audioFileType)

        if audioFileID is not None:
            audio = self.get_object(audio_ms, audioFileID)
            serializer = audio_ms.audio_serializer()
            serializer = serializer(audio)
            return Response(serializer.data, status=status.HTTP_200_OK)
                
        audio = audio_ms.audio_model().objects.all()
        serializer = audio_ms.audio_serializer()
        serializer = serializer(audio, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, 
            audioFileType = None,   
            format=None, *args, **kwargs):
            
        """
        CREATE AUDIO FILE REQUEST
        """
        
        if audioFileType not in AUDIO_FILE_TYPE:
            return Bad_Request()

        audio_ms = Audio_Model_Serializer(audioFileType)
        serializer = audio_ms.audio_serializer()
        serializer = serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, 
            audioFileType = None, audioFileID = None,  
            format=None, *args, **kwargs):
        """
        UPDATE AUDIO FILE REQUEST
        """

        if audioFileType not in AUDIO_FILE_TYPE:
            return Bad_Request()
        
        if audioFileID is None:
            return Response(
                {"message": "Please specify audioFileID"},
                status=status.HTTP_400_BAD_REQUEST)

        audio_ms = Audio_Model_Serializer(audioFileType)
        audio = self.get_object(audio_ms, audioFileID)
        serializer = audio_ms.audio_serializer()
        serializer = serializer(audio, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, 
            audioFileType = None, audioFileID = None, 
            format=None, *args, **kwargs):
        
        """
        DELETE FILE REQUEST
        """

        if audioFileType not in AUDIO_FILE_TYPE:
            return Bad_Request()

        if audioFileID is None:
            return Response({"message": "Please specify audioFileID"})

        audio_ms = Audio_Model_Serializer(audioFileType)
        audio = self.get_object(audio_ms, audioFileID)
        audio.delete()

        return Response({"message": "Deleted"}, status=status.HTTP_200_OK)



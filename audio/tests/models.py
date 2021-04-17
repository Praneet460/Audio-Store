# tests/models.py
################################
# AUTHOR : PRANEET NIGAM
################################
import datetime
from django.test import TestCase
from ..models import Song, Podcast, Audiobook

class AudioTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.new_song = Song.objects.create(
                            audio_title = "End of Time",
                            audio_duration = 187)

        cls.new_podcast = Podcast.objects.create(
                            audio_title = "Linear Programming",
                            audio_duration = 360,
                            host = "David Amos")

        cls.new_audiobook = Audiobook.objects.create(
                            audio_title = "The Secret Garden",
                            audio_duration = 12000,
                            author = "Frances Hodgson",
                            narrator = "DBS")

        cls.default_song = Song.objects.create()
        cls.default_podcast = Podcast.objects.create()
        cls.default_audiobook = Audiobook.objects.create()

    def test_audio_model(self):

        self.assertEqual(self.new_song.audio_title, 'End of Time')
        self.assertEqual(self.new_song.audio_duration, 187)
        self.assertEqual(self.new_podcast.audio_title, 'Linear Programming')
        self.assertEqual(self.new_podcast.audio_duration, 360)
        self.assertEqual(self.new_podcast.host, 'David Amos'),
        self.assertEqual(self.new_audiobook.audio_title, 'The Secret Garden')
        self.assertEqual(self.new_audiobook.audio_duration, 12000)
        self.assertEqual(self.new_audiobook.author, 'Frances Hodgson')
        self.assertEqual(self.new_audiobook.narrator, 'DBS')

    def test_song_model(self):

        self.assertEqual(self.default_song.audio_title, 'New Title')
        self.assertEqual(self.default_song.audio_duration, 0)

    def test_podcast_model(self):

        self.assertEqual(self.default_podcast.audio_title, 'New Title')
        self.assertEqual(self.default_podcast.audio_duration, 0)
        self.assertEqual(self.default_podcast.host, 'New Host')

    def test_audiobook_model(self):

        self.assertEqual(self.default_audiobook.audio_title, 'New Title')
        self.assertEqual(self.default_audiobook.audio_duration, 0)
        self.assertEqual(self.default_audiobook.author, 'New Author')
        self.assertEqual(self.default_audiobook.narrator, 'New Narrator')

    

    



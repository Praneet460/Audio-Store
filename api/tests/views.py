# api/tests/views.py

from django.test import TestCase
from django.urls import reverse

from audio.models import Song, Podcast, Audiobook
import json


class AudioViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.new_song = Song.objects.create(
                            audio_title = "End of Time",
                            audio_duration = 187)

        cls.new_audiobook = Audiobook.objects.create(
                            audio_title = "The Secret Garden",
                            audio_duration = 12000,
                            author = "Frances Hodgson",
                            narrator = "DBS")
        
        cls.song_data = {
                    "audio_title": "Faded",
                    "audio_duration": 190}
        
        cls.audiobook_data = {
                    "audio_title": "Into The Snow",
                    "audio_duration": 10000,
                    "author": "Nikolas",
                    "narrator": "ADB"}

    def test_song_view(self):
        
        resp = self.client.get('/api/v1/song/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('id' in resp.json()[0])
        self.assertTrue('audio_title' in resp.json()[0])
        self.assertTrue('audio_duration' in resp.json()[0])
        self.assertTrue('date_uploaded' in resp.json()[0])
        self.assertEqual([d['id'] for d in resp.json()], [1])
        self.assertEqual([d['audio_title'] for d in resp.json()], ['End of Time'])
        self.assertEqual([d['audio_duration'] for d in resp.json()], [187])

        resp = self.client.get('/api/v1/song/1')
        self.assertEqual(resp.status_code, 200)
        
        resp = self.client.get('/api/v1/song/2')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.post('/api/v1/song/', json.dumps(self.song_data),
                        content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_audiobook_view(self):

        resp = self.client.get('/api/v1/audiobook/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('id' in resp.json()[0])
        self.assertTrue('audio_title' in resp.json()[0])
        self.assertTrue('audio_duration' in resp.json()[0])
        self.assertTrue('date_uploaded' in resp.json()[0])
        self.assertTrue('author' in resp.json()[0])
        self.assertTrue('narrator' in resp.json()[0])
        self.assertEqual([d['id'] for d in resp.json()], [1])
        self.assertEqual([d['audio_title'] for d in resp.json()], ['The Secret Garden'])
        self.assertEqual([d['audio_duration'] for d in resp.json()], [12000])
        self.assertEqual([d['author'] for d in resp.json()], ['Frances Hodgson'])
        self.assertEqual([d['narrator'] for d in resp.json()], ['DBS'])

        resp = self.client.get('/api/v1/audiobook/1')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/api/v1/audiobook/2')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.post('/api/v1/audiobook/', json.dumps(self.audiobook_data),
                        content_type='application/json')
        self.assertEqual(resp.status_code, 201)





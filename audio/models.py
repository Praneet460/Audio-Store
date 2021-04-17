# models.py
##########################
# AUTHOR : PRANEET NIGAM
##########################

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Audio(models.Model):
    """
    Audio Abstract Class

    """

    audio_title = models.CharField(
                        max_length=100, 
                        default="New Title", 
                        verbose_name="Audio Title",
                        blank=False,
                        help_text="Type your Audio Title")

    audio_duration = models.PositiveIntegerField(
                        blank=False,
                        default=0,
                        help_text="Type your Audio Duration in seconds",
                        verbose_name="Audio Duration")

    date_uploaded = models.DateTimeField(
                        auto_now_add=True,
                        blank = False,
                        verbose_name="Audio Uploaded Time")

    date_updated = models.DateTimeField(
                        auto_now=True, 
                        verbose_name="Last Updated")

    class Meta:
        abstract = True


class Song(Audio):
    """
    Song Class inherits from Audio (Abstract Class)
    """
    
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ["id"]

    def __str__(self):
        return self.audio_title

class Podcast(Audio):
    """
    Podcast Class inherits from Audio (Abstract Class)
    """
    
    class Meta:
        verbose_name = "Podcast"
        verbose_name_plural = "Podcasts"
        ordering = ["id"]

    host = models.CharField(
                        max_length = 100,
                        default = "New Host",
                        verbose_name = "Podcast Host",
                        blank = False,
                        help_text="Type your Host Name")

    participants = ArrayField(
                        models.CharField(
                                max_length=100,
                                verbose_name="Participant Name",
                                blank = True,
                                help_text="Type your Participant Name"),
                        size = 10)

    def __str__(self):
        return self.audio_title

class Audiobook(Audio):
    """
    Audiobook Class inherits from Audio (Abstract Class)
    """
    
    class Meta:
        verbose_name = "Audiobook"
        verbose_name_plural = "Audiobooks"
        ordering = ["id"]

    author = models.CharField(
                    max_length = 100,
                    default = "New Author",
                    verbose_name = "Audiobook Author",
                    blank = False,
                    help_text="Type your Audiobook Author")

    narrator = models.CharField(
                    max_length = 100,
                    default = "New Narrator",
                    verbose_name = "Audiobook Narrator",
                    blank = False,
                    help_text="Type your Audiobook Narrator")

    def __str__(self):
        return self.audio_title
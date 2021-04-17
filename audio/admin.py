from django.contrib import admin
from .models import Song, Podcast, Audiobook

admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)


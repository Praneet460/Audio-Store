# urils.py

from django.urls import path, include
from .views import AudioView

app_name = 'api'

# API Endpoints
urlpatterns = [
    path('<str:audioFileType>/', AudioView.as_view(), name="audio-view"),
    path('<str:audioFileType>/<int:audioFileID>', AudioView.as_view(), name="audiodetail-view"),
]


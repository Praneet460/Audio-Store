## Project Name - Audio Store
It is an Audio Store API, build purely using Python (programming language), Django and Django-Rest-Framework (opensource framework written in python).
The Audio Store contains 3 types of audio files - <b>Song</b>, <b>Podcast</b> and <b>Audiobook</b> . The API provide you access to <b>GET</b>, <b>POST</b>, <b>PUT</b> and <b>DELETE</b> requests.

### Setup settings
- <b>src/manage.py</b> : src.settings.development (Prefer) / src.settings.production 
- pip install requirements.txt
- python manage.py test
- python manage.py runserver

### Files Path
- <b>Audio File Type Models :</b> audio.models
- <b>Audio File Type Models Tests :</b> audio.tests.models
- <b>Audio File Type API View :</b> api.views
- <b>Audio File Type API View Tests :</b> api.tests.views

### API EndPoints
API Endpoints defines the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

<b>BASE URL :</b> ```/api/v1```

| Endpoint | HTTP Method | CURD Method | Result |
|---|---|---|---|
| ```song/``` | POST | CREATE | Create a new song |
| ```podcast/``` | POST | CREATE | Create a new podcast |
| ```audiobook/``` | POST | CREATE | Create a new audiobook |
| ```song/<int:audioFileID>``` | GET  | READ  | Get a song details |
| ```song/``` | GET  | READ  | Get all songs details |
| ```podcast/<int:audioFileID>``` | GET  | READ  | Get a podcast details |
| ```podcast/``` | GET  | READ  | Get all podcast details |
| ```audiobook/<int:audioFileID>``` | GET  | READ  | Get an audiobook details |
| ```audiobook/``` | GET  | READ  | Get all audiobook details |
| ```song/<int:audioFileID>``` | PUT  | UPDATE  | UPDATE a song details |
| ```podcast/<int:audioFileID>``` | PUT  | UPDATE  | UPDATE a podcast details |
| ```audiobook/<int:audioFileID>``` | PUT  | UPDATE  | UPDATE an audiobook details |
| ```song/<int:audioFileID>``` | DELETE  | DELETE  | UPDATE a song details |
| ```podcast/<int:audioFileID>``` | DELETE  | DELETE  | UPDATE a podcast details |
| ```audiobook/<int:audioFileID>``` | DELETE  | DELETE  | UPDATE an audiobook details |

### Examples

- <b>GET :</b> ```/api/v1/song/
    - <b>Response</b>
        ```
        [
            {
                "id": 1,
                "audio_title": "End of Time",
                "audio_duration": 188,
                "date_uploaded": "2021-04-16T19:59:58.143261Z"
            },
            {
                "id": 2,
                "audio_title": "Faded",
                "audio_duration": 180,
                "date_uploaded": "2021-04-17T02:23:32.653622Z"
            },
            {
                "id": 7,
                "audio_title": "Sunshine",
                "audio_duration": 198,
                "date_uploaded": "2021-04-17T06:42:46.813823Z"
            }
        ]
        ```
- <b>PUT :</b> ```/api/v1/audiobook/1```
    - <b>Request</b>
        ```
        {
            "audio_title": "The Secret Garden",
            "audio_duration": 12000,
            "author": "Frances Hodgson",
            "narrator": "DBS"
        }
        ```
    - <b>Response</b>
        ```
        {
            "id": 1,
            "audio_title": "The Secret Garden",
            "audio_duration": 12000,
            "date_uploaded": "2021-04-16T20:02:07.549360Z",
            "author": "Frances Hodgson",
            "narrator": "DBS"
        }
        ```
- <b>POST :</b> ```/api/v1/podcast/1```
    - <b>Request</b>
        ```
        {
            "audio_title": "Python Basics",
            "audio_duration": 400,
            "host": "Alex",
            "participants": ["Praneet", "Robert", "William"] 
        }
        ```

- <b>DELETE :</b> ```/api/v1/song/3```
    - <b>Response</b>
    ```
    {
        "message": "Deleted"
    }
    ```

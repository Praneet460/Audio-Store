# development.py (settings)

from .base import *

# Debug turned on in development!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000"
]
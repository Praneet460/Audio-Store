# production.py (settings)

from .base import *

# Debug turned off in production!
DEBUG = False

ALLOWED_HOSTS = ['audioplayerstore.herokuapp.com']
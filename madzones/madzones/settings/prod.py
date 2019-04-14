from madzones.settings.base import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_files")
    # BASE_DIR is where manage.py lives. os.path.dirname code goes one step up the manage.py

STATIC_URL = "/assets/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

MEDIA_URL = '/media/'

SECRET_KEY = "change@it@to@your@own"

ALLOWED_HOSTS = [
    "127.0.0.1:8000"
    "127.0.0.1"
]
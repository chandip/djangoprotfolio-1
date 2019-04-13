from madzones.settings.base import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR, "assets"))
# BASE_DIR is where manage.py lives. above code goes one step up the manage.py

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")


SECRET_KEY = "asdfasefsdfef3323654DDDcdsaESDG2"

ALLOWED_HOSTS = [
    "127.0.0.1:8000"
    "127.0.0.1"
]


# from madzones.settings.base import *
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "asdfasefsdfef3323654DDDcdsaESDG2"
#
# ALLOWED_HOSTS = ["*"]
#

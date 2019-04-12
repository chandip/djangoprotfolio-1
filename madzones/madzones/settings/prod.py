from madzones.settings.base import *

DEBUG = False

STATIC_URL = '/assets/'
STATIC_ROOT = "/static_files"
MEDIA_URL = '/media/'

SECRET_KEY = "asdfasefsdfef3323654DDDcdsaESDG2"

ALLOWED_HOSTs = [
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

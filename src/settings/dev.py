from .base import *

ENVIRONMENT="development"
DEBUG = True
ALLOWED_HOSTS += ["*"]

# ################### CORS #######################

CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# ################# STATIC FILES #####################

STATIC_URL = "/staticfiles/"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

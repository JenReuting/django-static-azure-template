import os
from .base import *

ENVIRONMENT = "production"
DEBUG = False

ALLOWED_HOSTS = []  #Update this for prod or move to env variables

# ################ STATIC FILES ####################

STATICFILES_STORAGE = 'core.utils.azure_storages.AzureStaticStorage'

AZURE_CUSTOM_DOMAIN = os.environ.get("AZURE_STORAGE_CUSTOM_DOMAIN")
STATIC_CONTAINER = os.environ.get('AZURE_STATIC_CONTAINER')

STATIC_URL = (f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_CONTAINER}/')

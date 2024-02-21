from .base import *

ENVIRONMENT="production"
DEBUG=False

ALLOWED_HOSTS = []  #Update this for prod or move to env variables

# ################ STATIC FILES ####################

STATIC_CONTAINER = os.environ.get('AZURE_STATIC_CONTAINER')
AZURE_URL = os.environ.get('AZURE_CUSTOM_DOMAIN')

STATIC_URL = (f'https://{os.environ.get(AZURE_CUSTOM_DOMAIN)}/{STATIC_CONTAINER}/')
STATICFILES_STORAGE = 'core.utils.azure_storages.AzureStaticStorage'

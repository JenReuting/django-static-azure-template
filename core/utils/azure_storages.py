import os
from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    account_name = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY")
    azure_container = os.environ.get("AZURE_STATIC_CONTAINER")
    expiration_secs = None
    overwrite_files = True


class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY")
    azure_container = os.environ.get("AZURE_MEDIA_CONTAINER")
    expiration_secs = None
    # file_overwrite = False

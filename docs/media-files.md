# Media Files

When a media file is uploaded, it does not get stored on the local project. Instead, it gets automatically uploaded to the Azure Storage Container. This is because we have created a custom storage backend class for media files (located at `~/core/utils/azure_storage.py`).

To test this out, you can go to the admin panel and create a new user and upload a profile picture for that user. Then, you can check the Azure Storage Container to see if the file has been uploaded. The domain should be `https://<your-storage-account-name>.blob.core.windows.net/<container-name>/profile-photos/<image-name.jpg>`. 
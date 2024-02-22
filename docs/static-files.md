# Static Files in Development

Django can serve static files during development. Static files can be placed either in the `static` directory of an app (like `~/users/static/`) or in the `static` directory in the root of the project (`~/static/`).

NOTE: since we want to collect BOTH static and media files to Azure Storage Containers, we have created custom storage backend classes for both (located at `~/core/utils/azure_storage.py`). This is because the default `AzureStorage` class provided by `django-storages` only supports static files.

These custom classes are referenced in the production settings in `DEFAULT_FILE_STORAGE = 'core.utils.azure_storages.AzureMediaStorage'` and
`STATICFILES_STORAGE = 'core.utils.azure_storages.AzureStaticStorage'`.

# Static Files in Production

When the command `collectstatic` is ran during deployment, all static files in the application will be uploaded to the Azure Storage Container specified in the _AZURE STORAGES_-related settings in `base.py`.

Once this has been completed, the application can then access the static files from the STATIC_URL specified in the settings/prod.py file. If you navigate to your Azure Storage Container, you should see all the static files that were uploaded.

**IMPORTANT:** When creating your Azure Container for your static files, make sure to set the access level to "Blob" (not "Private" or "Container"). This will allow the files to be publicly accessible.

**NOTE:** You can access your `AZURE_ACCOUNT_KEY` value in your Azure Portal by going to your Storage Account and clicking on "Access Keys" in the right-side panel.

# Testing Production Implementation

If you want to test the implementation of static files being collected to an Azure Storage Container, you can simply change your ENVIRONMENT variable to `production` before running `collectstatic`:

```
ENVIRONMENT=production python manage.py collectstatic
```

Before testing, it's good practice to create a new container in the Azure Storage Account to test the implementation (e.g. "test-static"). If you do this, don't forget to _temporarily_ change the `AZURE_CONTAINER` setting in dev.py to the new container name.

_Important: Don't forget to change the settings back before deploying!_

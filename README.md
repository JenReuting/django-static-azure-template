# django-ckeditor-azure-template


### Notes: 

This project contains a custom User model, as well as some useful base models and mixins.

*Django Storages*: This app uses Django-Storages [docs here](https://django-storages.readthedocs.io/en/latest/) along with the [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) package.

This app does *NOT* use Whitenoise: Since this was developed with the intent to a.) be a backend API, and b.) utilize CloudFront's CDN for image serving, I did NOT add in Whitenoise. That configuration shouldn't be too difficult and, if I get time, I'll create another branch. 

This app does *NOT* use Gunicorn: Since this template was build with the intention to upload the final projects to Azure App Service, I did NOT add Gunicorn since Azure App Service for Django uses that by default. You can even configure the startup command for the App Service (to add more workers, etc) directly in the portal. More information can be found [here](https://learn.microsoft.com/en-us/azure/developer/python/configure-python-web-app-on-app-service#django-startup-commands). 

### Installation

Complete installation instructions can be found within the project - `docs/setup.md`.
# django-ckeditor-azure-template

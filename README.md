# django-static-azure-template

This is a template for a basic Django project that uses Azure Storage Containers for static and media file handling. Read the Docs (within the project files) for more information. 

### Notes: 

Whitenoise: Since this was developed with the intent to a.) be a backend API, and b.) utilize CloudFront's CDN for image serving, I did NOT add in Whitenoise. That configuration shouldn't be too difficult and, if I get time, I'll create another branch. 

Gunicorn: Since this template was build with the intention to upload the final projects to Azure App Service, I did NOT add Gunicorn since Azure App Service for Django uses that by default. You can even configure the startup command for the App Service (to add more workers, etc) directly in the portal. More information can be found [here](https://learn.microsoft.com/en-us/azure/developer/python/configure-python-web-app-on-app-service#django-startup-commands). 

# Azure App Service

Azure App Service installs and runs Gunicorn by default, so we do not need to install or configure it in the application. 

If I want to add a custom startup command, I can do so in the Azure Portal under the "Configuration" section.

Example startup command that uses 4 workers and also specifies that the wsgi file is located at `src.wsgi`:
`gunicorn --workers=4 --bind=0.0.0.0:8000 src.wsgi:application
`

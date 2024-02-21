"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

env = os.environ.get('ENVIRONMENT', 'development')  # Default to 'development' if not set
if env == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.prod')
elif env == 'staging':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.staging')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.dev')

application = get_wsgi_application()
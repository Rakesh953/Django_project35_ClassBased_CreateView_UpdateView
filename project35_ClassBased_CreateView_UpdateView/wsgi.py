"""
WSGI config for project35_ClassBased_CreateView_UpdateView project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project35_ClassBased_CreateView_UpdateView.settings')

application = get_wsgi_application()

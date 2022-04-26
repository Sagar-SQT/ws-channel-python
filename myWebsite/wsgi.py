"""
WSGI config for myWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.wsgi import get_wsgi_application

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myWebsite.settings')

application = get_wsgi_application()

application = ProtocolTypeRouter({
    'http': application,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

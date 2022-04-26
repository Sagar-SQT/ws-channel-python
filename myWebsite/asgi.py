"""
ASGI config for myWebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myWebsite.settings')

# application = get_asgi_application()


#
# import os
# # import django
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
#
# # os.environ['DJANGO_SETTINGS_MODULE'] = 'myWebsite.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myWebsite.settings')
#
# # django.setup()
# django_asgi_app = get_asgi_application()
#
# import chat.routing
#
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

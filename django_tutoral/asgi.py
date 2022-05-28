# wsgi보다 성능이 조금 더 improve, 비동기식 웹서버, 배포 진행

"""
ASGI config for django_tutoral project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutoral.settings')

application = get_asgi_application()

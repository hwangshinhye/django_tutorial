# 웹서버 게이트웨이 인터페이스
# 배포시 사용

"""
WSGI config for django_tutoral project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutoral.settings')

application = get_wsgi_application()

"""JWT configuration extending the original settings without editing them."""
from datetime import timedelta
import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

from .settings import *  # noqa: F403

load_dotenv(BASE_DIR / '.env', override=False)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
JWT_SIGNING_KEY = os.environ.get('JWT_SIGNING_KEY', '')
if not SECRET_KEY or not JWT_SIGNING_KEY:
    raise ImproperlyConfigured('Define DJANGO_SECRET_KEY and JWT_SIGNING_KEY in .env or the environment.')
if len(JWT_SIGNING_KEY.encode('utf-8')) < 32:
    raise ImproperlyConfigured('JWT_SIGNING_KEY must contain at least 32 bytes.')

DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() in ('true', '1', 'yes')
ALLOWED_HOSTS = [host.strip() for host in os.environ.get(
    'DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1'
).split(',') if host.strip()]
ROOT_URLCONF = 'config.jwt_urls'
WSGI_APPLICATION = 'config.jwt_wsgi.application'
ASGI_APPLICATION = 'config.jwt_asgi.application'

REST_FRAMEWORK = {
    **globals().get('REST_FRAMEWORK', {}),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}


def positive_env_int(name, default):
    try:
        value = int(os.environ.get(name, default))
    except ValueError as exc:
        raise ImproperlyConfigured(f'{name} must be a positive integer.') from exc
    if value <= 0:
        raise ImproperlyConfigured(f'{name} must be a positive integer.')
    return value


SIMPLE_JWT = {
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': JWT_SIGNING_KEY,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=positive_env_int('JWT_ACCESS_TOKEN_MINUTES', 15)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=positive_env_int('JWT_REFRESH_TOKEN_DAYS', 1)),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'ROTATE_REFRESH_TOKENS': False,
    'UPDATE_LAST_LOGIN': False,
}

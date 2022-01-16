"""Importanciones del sistema"""
import sys
from decouple import config  # pylint: disable=wrong-import-order
from .base import *  # pylint: disable=wildcard-import,unused-wildcard-import, missing-module-docstring

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default=""),
        'USER': config('POSTGRES_USER', default=""),
        'PASSWORD': config('POSTGRES_PASSWORD', default=""),
        'HOST': config('POSTGRES_HOST', default=""),
        'PORT': config('POSTGRES_PORT', default=""),
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME_TEST', default=""),
        'USER': config('DB_USER_TEST', default=""),
        'PASSWORD': config('DB_PASS_TEST', default=""),
        'HOST': config('DB_SERVICE_TEST', default=""),
        'PORT': config('DB_PORT_TEST', default=""),
    }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default="")
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default="")
EMAIL_PORT = config('EMAIL_PORT', default="")
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default="")
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default="")
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default="")

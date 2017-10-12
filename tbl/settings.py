"""
Django settings for tbl project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from .config.apps import PRODUCTION_APPS, DEVELOPMENT_APPS
from .config.middleware import MIDDLEWARE
from .config.template import TEMPLATES
from .config.security import SECRET_KEY
from .config.database import DB_DEVELOPMENT, DB_PRODUCTION
from .config.password import AUTH_PASSWORD_VALIDATORS
from .config.files import STATIC_ROOT, MEDIA_ROOT, STATIC_URL, MEDIA_URL
from .config.user import (
    AUTH_USER_MODEL,
    LOGIN_URL,
    LOGOUT_URL,
    LOGIN_REDIRECT_URL,
    AUTHENTICATION_BACKENDS
)
from .config.internacionalization import (
    PORTUGUESE, ENGLISH,
    TIME_ZONE,
    INTERNATIONALIZATION,
    FORMAT_DATES,
    TIMEZONE_DATETIMES
)
import os

# development or production enviroment
MODE_ENVIROMENT = os.getenv('MODE_ENVIROMENT', 'development')

# secret key
SECRET_KEY

# middlewares
MIDDLEWARE

# Urls
ROOT_URLCONF = 'tbl.urls'

# Templates
TEMPLATES

# WSGI - Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tbl.wsgi.application'

# Authentication
AUTH_USER_MODEL
LOGIN_URL
LOGOUT_URL
LOGIN_REDIRECT_URL
AUTHENTICATION_BACKENDS

# Password validation
AUTH_PASSWORD_VALIDATORS

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = PORTUGUESE
USE_I18N = INTERNATIONALIZATION
USE_L10N = FORMAT_DATES
USE_TZ = TIMEZONE_DATETIMES
TIME_ZONE


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT
STATIC_URL
MEDIA_ROOT
MEDIA_URL


# Enviroments mode (development or production)
if MODE_ENVIROMENT == 'development':
    DEBUG = True
    DATABASES = DB_DEVELOPMENT
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INSTALLED_APPS = DEVELOPMENT_APPS
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = ['*']
elif MODE_ENVIROMENT == 'production':
    DEBUG = False
    DATABASES = DB_PRODUCTION
    INSTALLED_APPS = PRODUCTION_APPS
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = ['*']

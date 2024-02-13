from .base import *

# PRODUCTION DATABASE - TO SET
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production-db',
        'USER': 'production-user',
        'PASSWORD': 'production-password',
        'HOST': 'production-address',
        'PORT': '5432',
    }
}
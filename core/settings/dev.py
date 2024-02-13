from .base import *


# SQL LITE DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'dev_db.sqlite3',
    }
}
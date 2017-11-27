import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sideHustle',
        'USER': 'jon_w',
        'PASSWORD': 'amvd53',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True

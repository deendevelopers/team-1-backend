from .settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS.append('*')

# Application definition

INSTALLED_APPS = [
    'fr.apps.FrConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'frontrow.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
         'HOST': 'ec2-54-247-72-30.eu-west-1.compute.amazonaws.com',
        'NAME': 'dc4u0105i2ij39',
        'USER': 'jwzelpolwsjqgz',
        'PASSWORD': 'c497db389a9a4b98a487f77e6b4ed0248ef403c4c903acabb0b5fd63a4abef32',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

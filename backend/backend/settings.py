from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&jammu8oqr^kzj8!o=)4d$bnl5pgzqi_4trewpxox&r3s^o9$d'

DEBUG = True



# DEF. DE LA APLICACI�N

INSTALLED_APPS = [
    'material.theme.teal',
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tfg',
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

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['plantillas'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MATERIAL_ADMIN_SITE = {
    'FAVICON':  'favicon.ico',  # Admin site favicon (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
}

WSGI_APPLICATION = 'backend.wsgi.application'

# HOST

ALLOWED_HOSTS = ['192.168.1.138', 'localhost', '127.0.0.1', 'www.app-tfg.local']

# BASE DE DATOS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tfg',
        'USER': 'root',
        'PASSWORD': 'tfg2022',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# VALIDACI�N DE LAS CONTRASE�AS

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# INTERNACIALIZACI�N

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# FICHEROS EST�TICOS

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

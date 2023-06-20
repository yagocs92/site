"""
Django settings for mantenedor project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1cv77t0t=-!s&x3grk(o)^t9p%+2hox3=*dts_96qy8p+l5%k^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['recogitate.azurewebsites.net', 'recogitate.com.br']

CSRF_TRUSTED_ORIGINS = ['https://*.recogitate.azurewebsites.net', 'https://*.recogitate.com.br']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestor',
    'crispy_forms',
    'crispy_bootstrap5',
    'corsheaders', 
    'cloudinary',
    'cloudinary_example.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mantenedor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gestor.novos_context.lista_pendencias_recentes',
                'gestor.novos_context.lista_pendencias_antigas',
                'gestor.novos_context.lista_pendencias_vencidas',
                'gestor.novos_context.lista_desembolso',
                'gestor.novos_context.lista_pendmaq',
            ],
        },
    },
]

WSGI_APPLICATION = 'mantenedor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recogitate-database',
        # 'NAME': os.path.join(BASE_DIR, 'mydb'),
        'USER': 'gpjubvjkke',
        'PASSWORD': '1Lithium23',
        'HOST': 'recogitate-server.postgres.database.azure.com',
        'PORT': '5432', # 8000 is default
    }
}

import dj_database_url
import os

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default='postgres://gpjubvjkke:{1Lithium23}@recogitate-server.postgres.database.azure.com/postgres?sslmode=require',
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'gestor:geral'

LOGIN_URL = 'gestor:login'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


CLOUDINARY = cloudinary.config( 
  cloud_name = "drdomhyt2", 
  api_key = "956951786545254", 
  api_secret = "rYwEZu2Zv9tpmjp0L6pNeRmeB58" 
)
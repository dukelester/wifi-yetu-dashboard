# -*- encoding: utf-8 -*-


import os
from decouple import config
from unipath import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=False)
DEBUG = True
# DEBUG = False
# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1'),'my-dj-auth.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Enable the inner app
    'mpesa',
    'wifiyetu',
    'mpesa_api',
    'authentication',
    'social_django',

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
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "profile"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "/"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]











WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# heroku db config
# import dj_database_url
#
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
#############################################################
#############################################################


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dukelester'
# EMAIL_HOST_PASSWORD = 'duke2030'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Wifi-Yetu Team <noreply@wifi1-yetu.com>'



#social auth
SOCIAL_AUTH_FACEBOOK_KEY = '774477499771994'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8119d84b936afe86c879d91b203ebc68'  # App Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77htpwvjswoalf'  # App ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET =  'mgVtdRQulVCpRLHi'  # App Secret
SOCIAL_AUTH_TWITTER_KEY = 'pU84F0gySiD2poeLu1kQP8T5C'
SOCIAL_AUTH_TWITTER_SECRET = 'SMR0ZdexR23etQnsduLusEEvzLgvt9wd1xNh3m3w7BL3Et1BtQ'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True



GP_CLIENT_ID = '616150480902-gd4kp9krlbmdm57e6s995gltrhhpv71k.apps.googleusercontent.com'
GP_CLIENT_SECRET = 'v0QovwJ20BpV45yQpMhYVUsM'

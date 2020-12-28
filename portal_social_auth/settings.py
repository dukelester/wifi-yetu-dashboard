"""
Django settings for portal_social_auth project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uo8&6&b0amm!=ptt-t&$y76mq4-mtw41hs0)buomg1y!@nfo#*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'portal_social_auth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')

                 ],
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

WSGI_APPLICATION = 'portal_social_auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': BASE_DIR / 'db.sqlite3',
#     # }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auth',
        'PASSWORD': '2025',
        'USER' :'postgres',
        'PORT':'',
        'HOST':'localhost',

   }
}


#heroku database config
import dj_database_url

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = '/index/'
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
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False



STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),

    ]

STATIC_ROOT = 'staticfiles'
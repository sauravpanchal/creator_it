"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# from distutils.command.config import config
from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rwfxb2*8wvkydyr5h_+e^179&o+_%5i5zm!s-(wz%cva6t0t%0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "accounts",
    "rest_framework",
    "djoser",
    "corsheaders",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "build")],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_USERNAME,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": "localhost",
        "PORT": "8888"
    }
}

'''
EMail ID : .env/EMAIL_ID
Password : .env/EMAIL_PASSWORD
'''
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "team.creator.it@gmail.com"
EMAIL_HOST_PASSWORD = "rkcqtnnlshxjseew"
EMAIL_USE_TLS = True



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build/static")
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # "rest_framework.authentication.TokenAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
DOMAIN = "creator.it.com"
SITE_NAME = "Creator IT"
# https://djoser.readthedocs.io/en/latest/settings.html
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True, # If True, you need to pass re_password to /users/ endpoint, to validate password equality.
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True, # If True, change username endpoints will send confirmation email to user.
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True, # If True, change password endpoints will send confirmation email to user.
    "SEND_CONFIRMATION_EMAIL": True, # If True, register or activation endpoint will send confirmation email to user.
    "SET_PASSWORD_RETYPE": True, # If True, you need to pass re_new_password to /users/set_password/ endpoint, to validate password equality.
    "PASSWORD_RESET_CONFIRM_RETYPE": True, # If True, you need to pass re_new_password to /users/reset_password_confirm/ endpoint in order to validate password equality.
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}", # URL to your frontend password reset page. It should contain {uid} and {token} placeholders, e.g. #/password-reset/{uid}/{token}. You should pass uid and token to reset password confirmation endpoint.
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}", # URL to your frontend username reset page. It should contain {uid} and {token} placeholders, e.g. #/username-reset/{uid}/{token}. You should pass uid and token to reset password confirmation endpoint.
    "ACTIVATION_URL": "activate/{uid}/{token}", # URL to your frontend activation page. It should contain {uid} and {token} placeholders, e.g. #/activate/{uid}/{token}. You should pass uid and token to activation endpoint.
    "SEND_ACTIVATION_EMAIL": True, 
    "SERIALIZERS": {
        "user_create": "accounts.serializers.UserCreateSerializer",
        "user": "accounts.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
    # "EMAIL": {
    #     "activation": "core.email.ActivationEmail"
    # }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = "accounts.UserAccount"

# LOCAL DEVELOPMENT ONLY
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_ALL_CREDENTIALS = True
# CORS_ORIGIN_CREDENTIALS = True

# FOR OPERATIONALIZED ENVIRONMENT
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000']
# this is for corsheaders (pip)
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOWED_ORIGINS = [
# "https://127.0.0.1:3000"
# "https://127.0.0.1:3000"
# ]

# from corsheaders.defaults import default_headers

# CORS_ALLOW_HEADERS = default_headers + ('',)
CORS_ALLOW_HEADERS = ('accept-encoding','content-type', 'accept', 'origin', 'authorization', 'Token')
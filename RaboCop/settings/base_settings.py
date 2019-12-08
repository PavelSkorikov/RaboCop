"""
Django local settings for RaboCop project.
with use 'os.environ' and 'python-dotenv' module
"""
import os
from dotenv import load_dotenv

# в переменной BASE_DIR получаем путь к каталогу проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# загружаем переменные окружения из файла '.env'
load_dotenv(os.path.join(BASE_DIR, '.env'))

DEBUG = (os.getenv('DEBUG')) # устанавливаем режим с помощью переменной 'DEBUG' из .env
TEMPLATE_DEBUG = DEBUG

# задаем подключение к БД
DATABASES = {
     'default': {
         'ENGINE': os.getenv('DB_ENGINE'),
         'NAME': os.getenv('DB_NAME'),
         'USER' : os.getenv('DB_USER'),
         'PASSWORD' : os.getenv('DB_PASSWORD'),
         'HOST' : os.getenv('DB_HOST'),
         'PORT' : os.getenv('DB_PORT'),
     }
 }

# считываем имена разрешенных хостов 'LOCAL_HOST' из .env
ALLOWED_HOSTS = [os.getenv('LOCAL_HOST')]

# считываем секр. ключ 'SECRET_KEY' из .env
SECRET_KEY = os.getenv('SECRET_KEY')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_summernote',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'FindJob',
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

ROOT_URLCONF = 'RaboCop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, os.getenv('TEMPLATES_PATH'))]
        ,
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

WSGI_APPLICATION = 'RaboCop.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, os.getenv('STATIC_PATH'))
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv('MEDIA_PATH'))
MEDIA_URL = '/media/'


import os

getenv = os.environ.get

BASE_DIR = getenv(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = getenv(
    'DJANGO_SECRET_KEY',
    '828)$0s0%-zpk2tfuj=!kdj52@%1r@e2zm%ys9nifpza^y*bx(')

DEBUG = bool(getenv('DJANGO_DEBUG', None))


ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '') \
    .strip() \
    .split()


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'djangoexample.accounts',
]


if DEBUG:
    INSTALLED_APPS += [
        'django_pdb',
        'debug_toolbar',
    ]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoexample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangoexample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': getenv('DJANGO_DB_DJANGOEXAMPLE_ENGINE',
                         'django.db.backends.sqlite3'),
        'NAME': getenv('DJANGO_DB_DJANGOEXAMPLE_NAME', 'djangoexample_db'),
        'HOST': getenv('DJANGO_DB_DJANGOEXAMPLE_HOST', '127.0.0.1'),
        'PORT': int(getenv('DJANGO_DB_DJANGOEXAMPLE_PORT', '3306')),
        'USER': getenv('DJANGO_DB_DJANGOEXAMPLE_USER', 'guest'),
        'PASSWORD': getenv('DJANGO_DB_DJANGOEXAMPLE_PASSWORD',
                           'tseug'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = getenv('DJANGO_LANGUAGE_CODE', 'en-us')

TIME_ZONE = getenv('DJANGO_TIME_ZONE', 'Asia/Tokyo')

USE_I18N = getenv('DJANGO_USE_I18N', None)

USE_L10N = getenv('DJANGO_USE_L10N', None)

USE_TZ = getenv('DJANGO_USE_TZ', None)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

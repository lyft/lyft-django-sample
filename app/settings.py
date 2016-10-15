"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jsonify',
    'social.apps.django_app.default',
    'adminrestrict',
    'app',
    'services',
    'home'
)

MIDDLEWARE_CLASSES = (
    'services.middleware.SSLMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'adminrestrict.middleware.AdminPagesRestrictMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.lyft.LyftOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Uncomment for Heroku
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='sqlite://django-rest-apis.db')
}

# Uncomment for local database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

# security: https://docs.djangoproject.com/en/1.9/ref/middleware/#module-django.middleware.security
SECURE_HSTS_SECONDS = 31536000 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# security: https://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
CSP_DEFAULT_SRC = ("'self'", 'https://www.google.com', )
CSP_IMG_SRC = ("'self'", 'https://www.google-analytics.com', 'https://*.googleapis.com', 'https://*.gstatic.com', 'https://s3.amazonaws.com', 'https://*.s3.amazonaws.com', )
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", 'https://www.google-analytics.com', 'https://*.googleapis.com', 'https://*.gstatic.com', 'https://www.google.com')
CSP_FRAME_SRC = ("'self'",'https://www.google.com' )
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'https://*.googleapis.com', 'https://*.gstatic.com')
CSP_FONT_SRC = ("'self'", 'https://*.googleapis.com', 'https://*.gstatic.com' )
CSP_OBJECT_SRC = ("'none'", )

SOCIAL_AUTH_LOGIN_URL          = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home'
SOCIAL_AUTH_LOGIN_ERROR_URL    = '/login-error/'

LOGIN_URL = '/login/lyft'

SOCIAL_AUTH_LYFT_KEY = environ.get('LYFT_KEY') # Client ID
SOCIAL_AUTH_LYFT_SECRET = environ.get('LYFT_SECRET') # Client Secret

SOCIAL_AUTH_LYFT_SCOPE = ['public', 'profile', 'rides.read', 'rides.request']

LYFT_YAML = 'file://' + os.path.join(BASE_DIR, 'lyft-api.yml')

GOOGLE_MAPS_JAVASCRIPT_KEY = environ.get('GOOGLE_MAPS_JAVASCRIPT_KEY')

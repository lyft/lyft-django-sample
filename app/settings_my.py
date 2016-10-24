try:
    from app.settings import *
except ImportError, exp:
    pass

DEBUG = True
SECRET_KEY = ''

SOCIAL_AUTH_LYFT_KEY = ''
SOCIAL_AUTH_LYFT_SECRET = ''

SOCIAL_AUTH_LYFT_SCOPE = ['public', 'profile', 'rides.read', 'rides.request']

LYFT_YAML = 'file://' + os.path.join(BASE_DIR, 'lyft-api.yml')

GOOGLE_MAPS_JAVASCRIPT_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

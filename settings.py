import os.path, sys
from urlparse import urljoin

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
 
ADMINS = (
   ('Sarp Erdag', 'sarp.erdag@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr-TR'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static")
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qgq8=gg8p-_4!ez@bt&ff+tg8s-zzq*sc_85w%bt62i@gy8j*+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'jcebooks.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates").replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    'books',
    'tagging',
    'feedbacks',
    'sorl.thumbnail',
)

try:
    from localsettings import *
except ImportError:
    print "Cannot import from localsettings.py"
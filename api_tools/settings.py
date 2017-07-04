import environ
import importlib

root = environ.Path(environ.os.getenv('API_ROOT'))
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env(root('.env'))

PROJECT_ROOT = root()
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

STATIC_URL = '/static/'


# Настройки Django
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
USE_I18N = USE_L10N = USE_TZ = True
ALLOWED_HOSTS = []

EXTRA_APPS = [
    'jet.dashboard',
    'jet',
]

# Используемые модули
COMMON_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'draceditor',
]
PROJECT_APPS = []



# Мидлварь
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Шаблоны
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


# БД
DATABASES = {
    'default': env.db()
}

AUTH_PASSWORD_VALIDATORS = []

# Rest Framework
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
project_settings = importlib.import_module(environ.os.getenv('PROJECT_SETTINGS'))
for var in dir(project_settings):
    if not var.startswith('__'):
        if var == 'ROOT_URLCONF':
            globals()['PROJECT_URLCONF'] = getattr(project_settings, var)
        else:
            globals()[var] = getattr(project_settings, var)

INSTALLED_APPS = EXTRA_APPS + COMMON_APPS + THIRD_PARTY_APPS + PROJECT_APPS
ROOT_URLCONF = 'api_tools.urls'
# Django debug tool bar
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
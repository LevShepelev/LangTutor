"""
Django settings for LangTutor project.
"""

from pathlib import Path

# Базовый каталог проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (замените на свой в production!)
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Режим отладки (не используйте DEBUG=True в production)
DEBUG = True

ALLOWED_HOSTS = []

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Локальные приложения
    'apps.tutor',
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

ROOT_URLCONF = 'langtutor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apps' / 'tutor' / 'templates'],
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

WSGI_APPLICATION = 'langtutor.wsgi.application'

# Настройка базы данных (SQLite для простоты)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Интернационализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'apps' / 'tutor' / 'static']

# Поле по умолчанию для первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Конфигурация для ограничения запросов к Mistral API (не более 1 запроса в секунду)
MISTRAL_API_RATE_LIMIT = 1

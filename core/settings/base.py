# Configuração de CORS: ajuste conforme necessário
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# TODO se quiser liberar todo mundo
# CORS_ALLOWED_ORIGINS = True


ROOT_URLCONF = "core.urls"
from pathlib import Path
from decouple import config
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="*",
    cast=lambda v: v.split(","),
)

INSTALLED_APPS = [
    "corsheaders",  # CORS support
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_extensions",
    "accounts",
    "companies",
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        # Backend do banco de dados
        "ENGINE": "django.db.backends.mysql",
        # Nome do banco de dados
        "NAME": config("DB_NAME", default="sge_db"),
        # Usuário do banco de dados
        "USER": config("DB_USER", default="root"),
        # Senha do banco de dados
        "PASSWORD": config("DB_PASSWORD", default=""),
        # Host do banco de dados
        "HOST": config("DB_HOST", default="localhost"),
        # Porta do banco de dados
        "PORT": config("DB_PORT", default="3306"),
        # Opções adicionais de conexão
        "OPTIONS": {
            # Define modo SQL estrito para integridade
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

LANGUAGE_CODE = "pt-br"
TIME_ZONE = config("TIME_ZONE", default="America/Belem")
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Define o modelo de usuário customizado
AUTH_USER_MODEL = "accounts.CustomUser"


# TODO adicionar configuração do djangorestframework-simplejwt
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(days=1)}

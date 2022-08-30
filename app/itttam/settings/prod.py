import environ
import os
from .base import *


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)

if READ_DOT_ENV_FILE:
    env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = os.environ.get("DEBUG")

SECRET_KEY = os.environ.get("SECRET_KEY")

# ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# EMAIL_BACKEND = env(
#     "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
# )

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "HOST": os.environ.get("SQL_HOST"),
        "NAME": os.environ.get("SQL_DBNAME"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "PORT": os.environ.get("SQL_PORT"),
    },
}

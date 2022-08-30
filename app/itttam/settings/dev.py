import environ
import os
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


env.read_env(os.path.join(BASE_DIR, ".devenv"))

DEBUG = env("DEV_DEBUG")

SECRET_KEY = env("DEV_SECRET_KEY")

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")


DATABASES = {
    "default": {
        "ENGINE": env("DEV_SQL_ENGINE"),
        "HOST": env("DEV_SQL_HOST"),
        "NAME": env("DEV_SQL_DBNAME"),
        "USER": env("DEV_SQL_USER"),
        "PASSWORD": env("DEV_SQL_PASSWORD"),
        "PORT": env("DEV_SQL_PORT"),
    }
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

INSTALLED_APPS += ["django_extensions"]

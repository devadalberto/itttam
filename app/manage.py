#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

# change this filename when running dev/prod
env_file_name = ".devenv"
# env_file_name = ".env"

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

DEBUG = env("DEBUG")

env.read_env(os.path.join(BASE_DIR, env_file_name))


def main():
    """Run administrative tasks."""

    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acity.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          env("DJANGO_SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

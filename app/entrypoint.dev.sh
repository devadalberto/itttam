#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DEV_SQL_HOST $DEV_SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate --run-syncdb
# python manage.py migrate
python manage.py runserver 0.0.0.0:9000 --settings $PROJECT_NAME.settings.$APP_ENVIRONMENT

exec "$@"

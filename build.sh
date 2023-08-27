#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Static files
mkdir static
python manage.py collectstatic --no-input

# Restart database
python manage.py flush --no-input

python manage.py makemigrations weapons

python manage.py migrate weapons

python manage.py migrate


# Insert new data
python manage.py seed weapons --number=5 
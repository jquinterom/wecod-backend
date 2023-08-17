#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Static files
python manage.py collectstatic --no-input

# Restart database
python manage.py flush
print('yes')

python manage.py makemigrations
python manage.py migrate

# Insert new data
python manage.py seed weapons --number=5 
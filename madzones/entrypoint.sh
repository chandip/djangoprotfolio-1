#!/bin/bash
python manage.py makemigrations
python manage.py makemigrations blogs courses pages quizes
python manage.py migrate
echo "Creating admin user"
echo "from django.contrib.auth import get_user_model;
 User = get_user_model();
 User.objects.create_superuser('test', 'test@myproject.com', 'test')" | python manage.py shell
exec "$@"
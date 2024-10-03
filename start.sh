# Ejecutar migraciones al iniciar la app
python manage.py makemigrations
python manage.py migrate
python createsuperuser.py

# Iniciar el servidor de Django
gunicorn wsgi.py

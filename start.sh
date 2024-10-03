# Ejecutar migraciones al iniciar la app
echo "EJECUTA LAS MIGRACIONES 
    AA
    A
    A
    A
    A
    A
    A

    A
    A
    A"
python manage.py makemigrations
python manage.py migrate
python createsuperuser.py

# Iniciar el servidor de Django
gunicorn judoyamato.wsgi

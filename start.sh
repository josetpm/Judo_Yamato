#!/usr/bin/env bash

# Mostrar mensaje en el log
echo "Ejecutando migraciones y creando superusuario..."

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario (esto debe ser automatizado o se debe modificar para no requerir entrada)
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true

# Mostrar mensaje en el log
echo "Iniciando el servidor con Gunicorn..."

# Iniciar el servidor Django
gunicorn judoyamato.wsgi:application --bind 0.0.0.0:$PORT

# Mostrar mensaje de éxito
echo "Servidor Django iniciado en el puerto $PORT"


#!/bin/bash
set -o errexit

# Instalar las dependencias desde el archivo requirements.txt
echo "Instalando dependencias..."
pip install -r requirements.txt

# Recopilar archivos estáticos sin interacción
echo "Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

# Crear migraciones
echo "Creando migraciones..."
python manage.py makemigrations

# Aplicar migraciones a la base de datos
echo "Aplicando migraciones..."
python manage.py migrate

# Crear un superusuario sin interacción, si no existe
echo "Creando superusuario..."
python manage.py createsuperuser --noinput --username superuser --password Pass_Word5 --email judo.yamato.club@gmail.com || true

echo "Proceso de construcción completado."

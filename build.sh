set -o errexit

pip install -r requirements.txt

python manage.py collectsatic --no-input
python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser --noinput --username admin --email admin@example.com || true

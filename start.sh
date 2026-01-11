#!/bin/sh

# Roda migrations
echo "Rodando migrations..."
python manage.py migrate --noinput

# Gera arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Inicia o Gunicorn
echo "Iniciando Gunicorn..."
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --log-level debug --access-logfile - --error-logfile -
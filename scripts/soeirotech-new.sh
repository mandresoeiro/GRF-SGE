#!/bin/bash
# Script de setup automatizado para o boilerplate Django

poetry install
poetry run python manage.py migrate
poetry run python manage.py createsuperuser --noinput || true
poetry run python manage.py collectstatic --noinput

echo "Setup concluído! Acesse o admin para criar o usuário manualmente se necessário."

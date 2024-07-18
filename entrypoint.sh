#!/bin/bash

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

flask db init || true
flask db migrate || true
flask db upgrade

exec "$@"
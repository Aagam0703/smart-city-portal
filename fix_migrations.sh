#!/bin/bash
echo "🔄 Fixing Database Migrations..."

echo "1. Checking migration status..."
docker-compose exec web python manage.py showmigrations

echo ""
echo "2. Creating migrations for core app..."
docker-compose exec web python manage.py makemigrations core

echo ""
echo "3. Creating migrations for data app..."
docker-compose exec web python manage.py makemigrations data

echo ""
echo "4. Applying all migrations..."
docker-compose exec web python manage.py migrate

echo ""
echo "5. Final migration status..."
docker-compose exec web python manage.py showmigrations

echo ""
echo "✅ Migration fix complete!"

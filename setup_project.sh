#!/bin/bash

echo "Setting up Smart City Portal Project..."

# Make manage.py executable
chmod +x manage.py

# Make scripts executable
chmod +x scripts/*.py

# Create necessary directories
mkdir -p logs
mkdir -p staticfiles

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file from .env.example"
    echo "Please update .env with your actual values"
fi

echo "Setup complete!"
echo ""
echo "To start the project:"
echo "1. Update .env with your actual values"
echo "2. Run: docker-compose up --build"
echo "3. Run migrations: docker-compose exec web python manage.py migrate"
echo "4. Create superuser: docker-compose exec web python manage.py createsuperuser"
echo "5. Access the application at http://localhost:8000"

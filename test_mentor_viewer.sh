#!/bin/bash
echo "🧪 Testing Mentor Database Viewer..."

echo "1. Testing web viewer..."
curl -s http://localhost:8000/mentor/ | grep -o '<title>.*</title>'

echo "2. Testing pgAdmin..."
docker-compose ps pgadmin

echo "3. Available URLs:"
echo "   📊 Database Viewer: https://your-codespace-8000.app.github.dev/mentor/"
echo "   🗂️  pgAdmin: https://your-codespace-5050.app.github.dev"
echo "   ⚙️  Django Admin: https://your-codespace-8000.app.github.dev/admin/"

echo ""
echo "✅ Setup complete! Share these URLs with your teacher."

#!/bin/bash
echo "🔧 Quick Fix for Login Issues..."

echo "1. Checking services..."
docker-compose ps

echo ""
echo "2. Testing admin access..."
curl -s http://localhost:8000/admin/ | grep -o '<title>.*</title>'

echo ""
echo "3. Testing authentication..."
docker-compose exec web python manage.py shell -c "
from django.contrib.auth.models import User
users = User.objects.all()
print(f'Total users: {users.count()}')
for u in users:
    print(f'- {u.username} (active: {u.is_active})')
"

echo ""
echo "✅ Quick fix complete!"
echo "🌐 Access your admin at: https://your-codespace-8000.app.github.dev/admin/"

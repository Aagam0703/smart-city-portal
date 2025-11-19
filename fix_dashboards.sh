#!/bin/bash
echo "🔧 Fixing Dashboard Pages..."

echo "1. Checking template files..."
ls -la templates/dashboard/

echo ""
echo "2. Testing dashboard URLs..."
echo "Services:"
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:8000/dashboard/services/
echo "Statistics:"
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:8000/dashboard/statistics/

echo ""
echo "3. Restarting web service..."
docker-compose restart web
sleep 3

echo ""
echo "4. Final test..."
curl -s http://localhost:8000/dashboard/services/ | grep -o '<title>.*</title>'
curl -s http://localhost:8000/dashboard/statistics/ | grep -o '<title>.*</title>'

echo ""
echo "✅ Dashboard fix complete!"
echo "🌐 Access your dashboards:"
echo "   Services: https://your-codespace-8000.app.github.dev/dashboard/services/"
echo "   Statistics: https://your-codespace-8000.app.github.dev/dashboard/statistics/"

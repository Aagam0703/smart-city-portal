#!/bin/bash
echo "🔍 Checking Website Accessibility..."

echo "1. Testing localhost access:"
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:8000/ || echo "Localhost failed"

echo "2. Testing health endpoint:"
curl -s http://localhost:8000/health/ | python -m json.tool 2>/dev/null || echo "Health check failed"

echo "3. Container status:"
docker-compose ps web

echo "4. Checking port binding:"
docker-compose port web 8000

echo ""
echo "✅ If you see HTTP Status: 200, your website is WORKING!"
echo "🌐 Access it via GitHub Codespaces port forwarding"

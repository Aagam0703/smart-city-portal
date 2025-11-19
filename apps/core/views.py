from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.db.utils import OperationalError
import redis
from redis.exceptions import ConnectionError as RedisConnectionError

class HealthCheckView(View):
    def get(self, request):
        # Check database connectivity
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = 'healthy'
        except OperationalError:
            db_status = 'unavailable'

        # Check Redis connectivity
        try:
            redis_client = redis.Redis(host='redis', port=6379, db=0, socket_connect_timeout=1)
            redis_client.ping()
            redis_status = 'healthy'
        except RedisConnectionError:
            redis_status = 'unavailable'

        # Overall status
        overall_status = 'healthy' if db_status == 'healthy' else 'degraded'

        return JsonResponse({
            'status': overall_status,
            'service': 'smart-city-portal',
            'database': db_status,
            'redis': redis_status
        })

class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Smart City Portal',
            'description': 'Comprehensive city data management and visualization platform'
        }
        return render(request, 'index.html', context)

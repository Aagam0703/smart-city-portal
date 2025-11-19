from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from apps.data.models import WeatherData, TransitData, ServiceRequest
from django.contrib.auth.models import User
from django.shortcuts import render

def mentor_database_viewer(request):
    """Database viewer that doesn't require login for demo purposes"""
    try:
        # Get all data from your models
        users = User.objects.all()
        weather_data = WeatherData.objects.all().order_by('-recorded_at')[:50]  # Limit to 50
        transit_data = TransitData.objects.all().order_by('-recorded_at')[:50]
        service_requests = ServiceRequest.objects.all().order_by('-reported_at')[:50]
        
        # Get database info
        with connection.cursor() as cursor:
            # Get table list
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cursor.fetchall()]
            
            # Get record counts
            table_counts = {}
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                table_counts[table] = cursor.fetchone()[0]
        
        context = {
            'users': users,
            'weather_data': weather_data,
            'transit_data': transit_data,
            'service_requests': service_requests,
            'tables': tables,
            'table_counts': table_counts,
            'total_records': sum(table_counts.values()),
            'tables_count': len(tables),
        }
        
    except Exception as e:
        context = {
            'error': str(e),
            'users': [],
            'weather_data': [],
            'transit_data': [],
            'service_requests': [],
            'tables': [],
            'table_counts': {},
            'total_records': 0,
            'tables_count': 0,
        }
    
    return render(request, 'mentor/database_viewer.html', context)

def database_schema(request):
    """Show database schema information"""
    try:
        with connection.cursor() as cursor:
            # Get table schema information
            cursor.execute("""
                SELECT 
                    table_name,
                    column_name,
                    data_type,
                    is_nullable,
                    column_default
                FROM information_schema.columns 
                WHERE table_schema = 'public'
                ORDER BY table_name, ordinal_position
            """)
            schema_data = cursor.fetchall()
        
        # Organize by table
        schema_by_table = {}
        for table_name, column_name, data_type, is_nullable, column_default in schema_data:
            if table_name not in schema_by_table:
                schema_by_table[table_name] = []
            schema_by_table[table_name].append({
                'column_name': column_name,
                'data_type': data_type,
                'is_nullable': is_nullable,
                'column_default': column_default
            })
        
        context = {'schema_by_table': schema_by_table}
        
    except Exception as e:
        context = {'error': str(e), 'schema_by_table': {}}
    
    return render(request, 'mentor/database_schema.html', context)

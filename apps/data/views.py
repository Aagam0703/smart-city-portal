from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import WeatherData, TransitData, ServiceRequest
from .serializers import (
    WeatherDataSerializer, 
    TransitDataSerializer, 
    ServiceRequestSerializer,
    DataSummarySerializer
)

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_data = WeatherData.objects.order_by('-recorded_at').first()
        serializer = self.get_serializer(latest_data)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        twenty_four_hours_ago = timezone.now() - timedelta(hours=24)
        data = WeatherData.objects.filter(recorded_at__gte=twenty_four_hours_ago)
        
        summary = {
            'total_records': data.count(),
            'cities': list(data.values_list('city', flat=True).distinct()),
            'avg_temperature': data.aggregate(models.Avg('temperature'))['temperature__avg'],
            'min_temperature': data.aggregate(models.Min('temperature'))['temperature__min'],
            'max_temperature': data.aggregate(models.Max('temperature'))['temperature__max'],
        }
        
        serializer = DataSummarySerializer(summary)
        return Response(serializer.data)

class TransitDataViewSet(viewsets.ModelViewSet):
    queryset = TransitData.objects.all()
    serializer_class = TransitDataSerializer
    
    @action(detail=False, methods=['get'])
    def current_status(self, request):
        latest_data = TransitData.objects.order_by('-recorded_at').first()
        serializer = self.get_serializer(latest_data)
        return Response(serializer.data)

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        stats = {
            'total_requests': ServiceRequest.objects.count(),
            'open_requests': ServiceRequest.objects.filter(status='open').count(),
            'in_progress_requests': ServiceRequest.objects.filter(status='in_progress').count(),
            'completed_today': ServiceRequest.objects.filter(
                status='completed',
                completed_at__date=timezone.now().date()
            ).count(),
            'by_type': list(ServiceRequest.objects.values('request_type').annotate(
                count=models.Count('id')
            ))
        }
        return Response(stats)

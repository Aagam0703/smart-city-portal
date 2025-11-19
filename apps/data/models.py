from django.db import models
from apps.core.models import TimeStampedModel

class WeatherData(TimeStampedModel):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=100)
    recorded_at = models.DateTimeField()
    
    class Meta:
        indexes = [
            models.Index(fields=['city', 'recorded_at']),
        ]
        ordering = ['-recorded_at']

class TransitData(TimeStampedModel):
    subway_delays = models.IntegerField()
    bus_delays = models.IntegerField()
    active_buses = models.IntegerField()
    active_trains = models.IntegerField()
    avg_wait_time = models.FloatField()
    recorded_at = models.DateTimeField()
    
    class Meta:
        indexes = [
            models.Index(fields=['recorded_at']),
        ]
        ordering = ['-recorded_at']

class ServiceRequest(TimeStampedModel):
    REQUEST_TYPES = [
        ('sanitation', 'Sanitation'),
        ('transportation', 'Transportation'),
        ('utilities', 'Utilities'),
        ('public_safety', 'Public Safety'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ]
    
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.IntegerField(default=1)  # 1-5, 5 being highest
    reported_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['request_type', 'status']),
            models.Index(fields=['reported_at']),
        ]
        ordering = ['-reported_at']

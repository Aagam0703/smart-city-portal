from rest_framework import serializers
from .models import WeatherData, TransitData, ServiceRequest

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class TransitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitData
        fields = '__all__'

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

class DataSummarySerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    cities = serializers.ListField(child=serializers.CharField())
    avg_temperature = serializers.FloatField(required=False)
    min_temperature = serializers.FloatField(required=False)
    max_temperature = serializers.FloatField(required=False)

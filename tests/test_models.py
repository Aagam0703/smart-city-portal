from django.test import TestCase
from django.utils import timezone
from apps.data.models import WeatherData, TransitData, ServiceRequest

class WeatherDataModelTest(TestCase):
    def setUp(self):
        self.weather_data = WeatherData.objects.create(
            city="Test City",
            temperature=22.5,
            humidity=65.0,
            pressure=1013.0,
            wind_speed=3.5,
            description="clear sky",
            recorded_at=timezone.now()
        )

    def test_weather_data_creation(self):
        self.assertEqual(self.weather_data.city, "Test City")
        self.assertEqual(self.weather_data.temperature, 22.5)
        self.assertTrue(isinstance(self.weather_data, WeatherData))

class TransitDataModelTest(TestCase):
    def setUp(self):
        self.transit_data = TransitData.objects.create(
            subway_delays=5,
            bus_delays=12,
            active_buses=245,
            active_trains=185,
            avg_wait_time=4.2,
            recorded_at=timezone.now()
        )

    def test_transit_data_creation(self):
        self.assertEqual(self.transit_data.subway_delays, 5)
        self.assertEqual(self.transit_data.bus_delays, 12)
        self.assertTrue(isinstance(self.transit_data, TransitData))

class ServiceRequestModelTest(TestCase):
    def setUp(self):
        self.service_request = ServiceRequest.objects.create(
            request_type="sanitation",
            description="Garbage collection missed",
            location="123 Main St",
            status="open",
            priority=2
        )

    def test_service_request_creation(self):
        self.assertEqual(self.service_request.request_type, "sanitation")
        self.assertEqual(self.service_request.status, "open")
        self.assertTrue(isinstance(self.service_request, ServiceRequest))

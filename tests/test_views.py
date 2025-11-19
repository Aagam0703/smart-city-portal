from django.test import TestCase, Client
from django.urls import reverse
from apps.data.models import WeatherData, TransitData
from django.utils import timezone

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.weather_data = WeatherData.objects.create(
            city="Test City",
            temperature=22.5,
            recorded_at=timezone.now()
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_health_check(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'healthy', 'service': 'smart-city-portal'}
        )

    def test_weather_api(self):
        response = self.client.get('/api/data/weather/')
        self.assertEqual(response.status_code, 200)

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_transit_dashboard(self):
        response = self.client.get('/dashboard/transit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/transit.html')

    def test_weather_dashboard(self):
        response = self.client.get('/dashboard/weather/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/weather.html')

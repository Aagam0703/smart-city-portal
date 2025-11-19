from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherDataViewSet, TransitDataViewSet, ServiceRequestViewSet

router = DefaultRouter()
router.register(r'weather', WeatherDataViewSet)
router.register(r'transit', TransitDataViewSet)
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

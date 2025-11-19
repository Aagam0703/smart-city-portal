from django.urls import path
from .views import DashboardView, MainDashboardView

urlpatterns = [
    path('', MainDashboardView.as_view(), name='dashboard-main'),
    path('<str:dashboard_type>/', DashboardView.as_view(), name='dashboard-view'),
]

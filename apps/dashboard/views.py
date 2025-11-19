from django.shortcuts import render
from django.views import View

class DashboardView(View):
    def get(self, request, dashboard_type):
        templates = {
            'transit': 'dashboard/transit.html',
            'weather': 'dashboard/weather.html',
            'services': 'dashboard/services.html',
            'statistics': 'dashboard/statistics.html',
        }
        
        template = templates.get(dashboard_type, 'dashboard/transit.html')
        context = {
            'dashboard_type': dashboard_type,
            'title': f'{dashboard_type.title()} Dashboard'
        }
        
        return render(request, template, context)

class MainDashboardView(View):
    def get(self, request):
        return render(request, 'index.html', {
            'title': 'Smart City Portal - Main Dashboard'
        })

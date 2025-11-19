from django.contrib import admin
from .models import City, Configuration

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'area', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'created_at']
    search_fields = ['key', 'value']
    list_filter = ['created_at']

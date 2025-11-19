from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_database_viewer, name='mentor-database-viewer'),
    path('schema/', views.database_schema, name='mentor-database-schema'),
]

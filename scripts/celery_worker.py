#!/usr/bin/env python
import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.data.tasks import fetch_all_data, process_all_data

if __name__ == '__main__':
    print("Starting Celery worker...")
    # This script is mainly for local development
    # In production, use: celery -A config worker --loglevel=info

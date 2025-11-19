# Smart City Portal

A comprehensive Django-based portal for smart city data management and visualization.

## Features

- Real-time data acquisition from various city services
- Interactive dashboards for transit, weather, and city services
- RESTful APIs for data access
- Celery for background task processing
- Docker containerization

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure variables
3. Run: `docker-compose up --build`
4. Access the application at `http://localhost:8000`

## Project Structure

- `apps/` - Django applications
- `config/` - Project configuration
- `scripts/` - Data processing scripts
- `static/` - Static files
- `templates/` - HTML templates
- `data/` - Data storage

## API Endpoints

- `/api/data/` - Data API
- `/dashboard/` - Interactive dashboards
- `/admin/` - Django admin
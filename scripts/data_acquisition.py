import requests
import pandas as pd
import json
import os
from datetime import datetime
import time

class DataAcquisition:
    def __init__(self):
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        self.transit_api_key = os.getenv('TRANSIT_API_KEY')
        
    def fetch_weather_data(self, city="New York"):
        """Fetch current weather data for a city"""
        try:
            # Mock weather data - replace with actual API call
            weather_data = {
                'city': city,
                'temperature': 22.5,
                'humidity': 65,
                'pressure': 1013,
                'description': 'clear sky',
                'wind_speed': 3.5,
                'timestamp': datetime.now().isoformat()
            }
            
            # Save to file
            filename = f"data/raw/weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(weather_data, f, indent=2)
                
            print(f"Weather data saved to {filename}")
            return weather_data
            
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def fetch_transit_data(self):
        """Fetch public transit data"""
        try:
            # Mock transit data
            transit_data = {
                'timestamp': datetime.now().isoformat(),
                'subway_delays': 3,
                'bus_delays': 12,
                'active_buses': 245,
                'active_trains': 185,
                'avg_wait_time': 4.2
            }
            
            filename = f"data/raw/transit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(transit_data, f, indent=2)
                
            print(f"Transit data saved to {filename}")
            return transit_data
            
        except Exception as e:
            print(f"Error fetching transit data: {e}")
            return None
    
    def fetch_city_services_data(self):
        """Fetch city services data"""
        try:
            services_data = {
                'timestamp': datetime.now().isoformat(),
                'open_311_requests': 156,
                'completed_requests_today': 89,
                'avg_response_time': 2.1,
                'emergency_calls': 23
            }
            
            filename = f"data/raw/services_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(services_data, f, indent=2)
                
            print(f"Services data saved to {filename}")
            return services_data
            
        except Exception as e:
            print(f"Error fetching services data: {e}")
            return None

if __name__ == "__main__":
    acquirer = DataAcquisition()
    
    print("Fetching weather data...")
    acquirer.fetch_weather_data()
    
    print("Fetching transit data...")
    acquirer.fetch_transit_data()
    
    print("Fetching services data...")
    acquirer.fetch_city_services_data()

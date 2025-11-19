import pandas as pd # pyright: ignore[reportMissingModuleSource]
import json
import os
from datetime import datetime, timedelta
import glob

class DataProcessor:
    def __init__(self):
        self.raw_data_path = "data/raw"
        self.processed_data_path = "data/processed"
        
    def process_weather_data(self):
        """Process and aggregate weather data"""
        try:
            weather_files = glob.glob(f"{self.raw_data_path}/weather_*.json")
            weather_data = []
            
            for file in weather_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    weather_data.append(data)
            
            if weather_data:
                df = pd.DataFrame(weather_data)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df = df.sort_values('timestamp')
                
                # Save processed data
                output_file = f"{self.processed_data_path}/weather_processed.csv"
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                df.to_csv(output_file, index=False)
                print(f"Weather data processed and saved to {output_file}")
                
                return df
            return None
            
        except Exception as e:
            print(f"Error processing weather data: {e}")
            return None
    
    def process_transit_data(self):
        """Process and aggregate transit data"""
        try:
            transit_files = glob.glob(f"{self.raw_data_path}/transit_*.json")
            transit_data = []
            
            for file in transit_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    transit_data.append(data)
            
            if transit_data:
                df = pd.DataFrame(transit_data)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df = df.sort_values('timestamp')
                
                # Calculate hourly averages
                df['hour'] = df['timestamp'].dt.hour
                hourly_avg = df.groupby('hour').agg({
                    'subway_delays': 'mean',
                    'bus_delays': 'mean',
                    'avg_wait_time': 'mean'
                }).reset_index()
                
                output_file = f"{self.processed_data_path}/transit_processed.csv"
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                df.to_csv(output_file, index=False)
                
                hourly_file = f"{self.processed_data_path}/transit_hourly.csv"
                hourly_avg.to_csv(hourly_file, index=False)
                
                print(f"Transit data processed and saved")
                return df
            return None
            
        except Exception as e:
            print(f"Error processing transit data: {e}")
            return None
    
    def process_services_data(self):
        """Process and aggregate services data"""
        try:
            services_files = glob.glob(f"{self.raw_data_path}/services_*.json")
            services_data = []
            
            for file in services_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    services_data.append(data)
            
            if services_data:
                df = pd.DataFrame(services_data)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df = df.sort_values('timestamp')
                
                output_file = f"{self.processed_data_path}/services_processed.csv"
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                df.to_csv(output_file, index=False)
                
                print(f"Services data processed and saved to {output_file}")
                return df
            return None
            
        except Exception as e:
            print(f"Error processing services data: {e}")
            return None
    
    def generate_daily_report(self):
        """Generate daily summary report"""
        try:
            weather_df = self.process_weather_data()
            transit_df = self.process_transit_data()
            services_df = self.process_services_data()
            
            report = {
                'report_date': datetime.now().isoformat(),
                'weather_records': len(weather_df) if weather_df is not None else 0,
                'transit_records': len(transit_df) if transit_df is not None else 0,
                'services_records': len(services_df) if services_df is not None else 0,
                'generated_at': datetime.now().isoformat()
            }
            
            report_file = f"{self.processed_data_path}/daily_report.json"
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
                
            print(f"Daily report saved to {report_file}")
            return report
            
        except Exception as e:
            print(f"Error generating daily report: {e}")
            return None

if __name__ == "__main__":
    processor = DataProcessor()
    
    print("Processing weather data...")
    processor.process_weather_data()
    
    print("Processing transit data...")
    processor.process_transit_data()
    
    print("Processing services data...")
    processor.process_services_data()
    
    print("Generating daily report...")
    processor.generate_daily_report()
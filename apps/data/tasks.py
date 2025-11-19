from celery import shared_task
from scripts.data_acquisition import DataAcquisition
from scripts.data_processing import DataProcessor
import logging

logger = logging.getLogger(__name__)

@shared_task
def fetch_weather_data():
    try:
        acquirer = DataAcquisition()
        result = acquirer.fetch_weather_data()
        logger.info("Weather data fetched successfully")
        return result
    except Exception as e:
        logger.error(f"Error fetching weather data: {e}")
        return None

@shared_task
def fetch_transit_data():
    try:
        acquirer = DataAcquisition()
        result = acquirer.fetch_transit_data()
        logger.info("Transit data fetched successfully")
        return result
    except Exception as e:
        logger.error(f"Error fetching transit data: {e}")
        return None

@shared_task
def fetch_services_data():
    try:
        acquirer = DataAcquisition()
        result = acquirer.fetch_city_services_data()
        logger.info("Services data fetched successfully")
        return result
    except Exception as e:
        logger.error(f"Error fetching services data: {e}")
        return None

@shared_task
def fetch_all_data():
    tasks = [fetch_weather_data, fetch_transit_data, fetch_services_data]
    results = []
    for task in tasks:
        result = task.delay()
        results.append(result)
    return [result.get() for result in results]

@shared_task
def process_all_data():
    try:
        processor = DataProcessor()
        weather_result = processor.process_weather_data()
        transit_result = processor.process_transit_data()
        services_result = processor.process_services_data()
        report_result = processor.generate_daily_report()
        
        logger.info("All data processed successfully")
        return {
            'weather': weather_result is not None,
            'transit': transit_result is not None,
            'services': services_result is not None,
            'report': report_result is not None
        }
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        return None

@shared_task
def daily_data_pipeline():
    fetch_all_data.delay()
    process_all_data.delay()
    logger.info("Daily data pipeline executed")

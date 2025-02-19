import logging
import json
from webscraping import scrape_and_export # Ensure the correct module name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Starting Scraper")

    try:
        scrape_and_export()  # Call the function from webscraping_2_0
        logger.info("Scraping completed successfully.")

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Firmware successfully scraped'})
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

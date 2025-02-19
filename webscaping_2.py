import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_firmware_versions(url, desired_device_types):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    mw_parser_output_div = soup.select_one('.mw-parser-output')

    if not mw_parser_output_div:
        logging.error("Couldn't find div with class 'mw-parser-output'")
        return {}

    wikitable_elements = mw_parser_output_div.find_all('table', class_='wikitable')
    firmware_dict = {}

    for table in wikitable_elements:
        tbody = table.find('tbody')
        if not tbody:
            continue

        rows = tbody.find_all('tr')
        headers = [header.get_text(strip=True) for header in rows[0].find_all(['th', 'td'])]
        rows = rows[1:] if any(headers) else rows

        for row in rows:
            columns = row.find_all(['th', 'td'])
            row_data = [col.get_text(strip=True) for col in columns]

            if len(row_data) < 4:
                continue

            device_type = row_data[0]
            firmware_version = row_data[3]# Ensure this correctly extracts firmware version

            if device_type in desired_device_types:
                firmware_dict[device_type] = firmware_version

    if not firmware_dict:
        logging.warning("No firmware data found for the specified device types.")

    return firmware_dict

# Define URL and device types
url = 'https://wiki.teltonika-gps.com/view/Firmware_versions'
desired_device_types = [
    'FMB001', 'FMB003', 'FMC001', 'FMC003', 'FMM001(BG96)', 'FMM003', 'FMC130SLM320', 'FMB204',
    'TAT100', 'TAT140', 'FMB140', 'FMC640', 'FMB130', 'FMP100', 'FMM00A'
]

# Execute scraping
firmware_versions = scrape_firmware_versions(url, desired_device_types)
logging.info(f"Firmware versions: {firmware_versions}")

__name__ = "__main__"
if __name__ == "__main__":
    logging.info("Starting scraper")
    scrape_firmware_versions(url, desired_device_types)
    logging.info("Scraper finished")
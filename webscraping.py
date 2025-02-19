import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def scrape_and_export(url, desired_device_types):
    print(f"Fetching data from {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    mw_parser_output_div = soup.select_one('.mw-parser-output')

    if not mw_parser_output_div:
        print("Couldn't find div with class 'mw-parser-output'")
        return

    wikitable_elements = mw_parser_output_div.find_all('table', class_='wikitable')

    data_list = []
    max_columns = 0

    for table in wikitable_elements:
        tbody = table.find('tbody')
        if not tbody:
            continue

        rows = tbody.find_all('tr')

        for row in rows:
            columns = row.find_all(['th', 'td'])
            row_data = [column.get_text(strip=True) for column in columns]

            if all('th' in column.name for column in columns):  # Skip header rows
                continue

            if len(row_data) > 2:
                row_data.pop(2)  # Remove column at index 2 if it exists

            filtered_row_data = [value for value in row_data if value]  # Remove empty values

            if filtered_row_data and filtered_row_data[0] in desired_device_types:
                print(f"Processed row data: {filtered_row_data}")

                max_columns = max(max_columns, len(filtered_row_data))
                data_list.append(filtered_row_data)

    if not data_list:
        print("No data found for the specified device types.")
        return

    # Normalize data (ensure all rows have the same number of columns)
    normalized_data = [row + [''] * (max_columns - len(row)) for row in data_list]

    df = pd.DataFrame(normalized_data)

    # Dynamic column naming
    column_names = ["Device Type", "Date of release", "Firmware Version", "Configurator type"]
    df.columns = column_names[:df.shape[1]]  # Adjust if fewer columns

    df.dropna(how='all', axis=1, inplace=True)  # Remove empty columns

    # Generate file name
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_filename = f'Firmware_data_{current_datetime}.xlsx'

    df.to_excel(excel_filename, index=False)
    print(f"Data has been exported to {excel_filename}")

# Example usage:
# scrape_and_export("https://example.com/wiki_page", ["Device A", "Device B"])


# Specify the URL for scraping
url = 'https://wiki.teltonika-gps.com/view/Firmware_versions'

# Specify the updated desired device types
desired_device_types = [
    'FMB001', 'FMB003', 'FMC001', 'FMC003', 'FMM001(BG96)', 'FMM003', 'FMC130SLM320', 'FMB204',
    'TAT100', 'TAT140', 'FMB140', 'FMC640', "FMB130", "FMP100", "FMM00A"
]

# Run the scraping and export function
scrape_and_export(url, desired_device_types)

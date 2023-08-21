import csv
import time
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize Chrome WebDriver
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

# Base URL for individual product pages
base_url = "https://www.amazon.in{}"

# List to store scraped data
data_list = []

# Read the list of product URLs from a file or generate it programmatically
product_urls = [
    "/dp/B08YYP1ZDC",  # Example product URL
    # Add more product URLs here
]

for product_url in product_urls:
    full_url = base_url.format(product_url)
    driver.get(full_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    asin = product_url.split("/")[-1]
    
    product_description_element = soup.find("div", {"id": "productDescription"})
    product_description = product_description_element.get_text() if product_description_element else "N/A"
    
    manufacturer_element = soup.find("a", {"id": "bylineInfo"})
    manufacturer = manufacturer_element.get_text() if manufacturer_element else "N/A"

    data_list.append({
        "Product URL": full_url,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer,
    })

# Quit the WebDriver
driver.quit()

# Export data to CSV
csv_filename = "scraped_data.csv"
csv_fields = ["Product URL", "ASIN", "Product Description", "Manufacturer"]

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    csv_writer.writeheader()
    csv_writer.writerows(data_list)

print("Data scraped and exported to", csv_filename)

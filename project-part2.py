import csv
import requests
from bs4 import BeautifulSoup

# List of product URLs
product_urls = [
    # Add your 200 product URLs here
]

# List to store scraped data
data_list = []

# Loop through the product URLs
for product_url in product_urls:
    # Send a GET request to the product URL
    response = requests.get(product_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract ASIN from URL
        asin = product_url.split("/")[-1]
        
        # Extract product description
        product_description_element = soup.find("div", {"id": "productDescription"})
        product_description = product_description_element.get_text() if product_description_element else "N/A"
        
        # Extract manufacturer
        manufacturer_element = soup.find("a", {"id": "bylineInfo"})
        manufacturer = manufacturer_element.get_text() if manufacturer_element else "N/A"
        
        # Append data to the list
        data_list.append({
            "Product URL": product_url,
            "ASIN": asin,
            "Product Description": product_description,
            "Manufacturer": manufacturer,
        })
    else:
        print(f"Failed to retrieve data for {product_url}")

# Export data to CSV
csv_filename = "scraped_data.csv"
csv_fields = ["Product URL", "ASIN", "Product Description", "Manufacturer"]

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    csv_writer.writeheader()
    csv_writer.writerows(data_list)

print("Data scraped and exported to", csv_filename)

import csv

# Read data from CSV file
csv_filename = "scraped_data.csv"
data_list = []

with open(csv_filename, "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data_list.append(row)

# Display the data
for data in data_list:
    print("Product URL:", data["Product URL"])
    print("ASIN:", data["ASIN"])
    print("Product Description:", data["Product Description"])
    print("Manufacturer:", data["Manufacturer"])
    print("-" * 200)


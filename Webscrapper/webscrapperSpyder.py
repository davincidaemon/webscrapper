import requests
from bs4 import BeautifulSoup
import csv

# URL and file name
url = "https://www.goodreads.com/genres/mystery"
filename = "goodreads.csv"

# Send HTTP request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data
books = soup.find_all('article', class_='product_pod')
data = []

for book in books:
    title = book.find('h3').text
    price = book.find('p', class_='price_color').text
    data.append([title, price])

# Store data in CSV file
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])  # header
    writer.writerows(data)

print("Data saved to", filename)

import requests
from bs4 import BeautifulSoup
import csv


website_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(website_url)


soup = BeautifulSoup(response.text, "lxml")


product_titles = soup.find_all("a", class_="title")
product_prices = soup.find_all("h4", class_="pull-right price")
product_reviews = soup.find_all("p", class_="pull-right")


scraped_data = []

for title, price, review in zip(product_titles, product_prices, product_reviews):
    title_text = title.text.strip()
    price_text = price.text.strip()
    review_count = review.text.strip()
    scraped_data.append([title_text, price_text, review_count])


output_file = "scraped_products.csv"


with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Reviews"])
    writer.writerows(scraped_data)

print(f"Scraped data has been saved to '{output_file}' successfully.")

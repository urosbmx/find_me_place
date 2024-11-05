import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

class WebScrape:

    LOCATION_URLS = {
        "blok_37": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-37",
        "blok_33": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-33",
        "blok_3": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-3",
        "blok_2": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-2",
        "blok_4": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-4"
    }

    def __init__(self, location):
        self.location = location

    def web_scraping(self):
        # Get the URL based on the location
        url = self.LOCATION_URLS.get(self.location, self.LOCATION_URLS["blok_37"])

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
        }

        try:
            # Send the request and get the page content
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all product items
            product_titles = soup.find_all(class_='product-list-item')

            # Extract product data
            rows = [
                (
                    title.get_text(strip=True),
                    price.get_text(strip=True),
                    price_per_m.get_text(strip=True),
                    f"https://www.halooglasi.com/{link['href']}"
                )
                for row in product_titles
                if (price := row.find(class_='central-feature')) and
                   (price_per_m := row.find(class_='price-by-surface')) and
                   (title := row.find(class_='product-title')) and
                   (link := row.find('a'))
            ]

            # Define table columns
            cols = ('Naziv', 'Cena', 'Cena €/m2', 'Link')

            # Generate and print the HTML table
            html_table = tabulate(rows, headers=cols, tablefmt='html')
            return html_table

        except Exception as e:
            print(f"An error occurred: {e}")
            return None  # Return None if an error occurs

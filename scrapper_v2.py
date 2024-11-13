import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from tabulate import tabulate


class WebScrape:
    def __init__(self, location):
        self.location = location

    def scrape_web(self):
        try:
            all_rows = []  # Initialize this outside the loop to collect all rows

            for location in self.location:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, '
                                  'like Gecko) Version/17.5 Safari/605.1.15',
                }
                response = requests.get(location["link"], headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                place = soup.find_all(class_='product-list-item')

                for row in place:
                    publis_data = row.find(class_='publish-date')
                    price = row.find(class_='central-feature')
                    price_per_m = row.find(class_='price-by-surface')
                    title = row.find(class_='product-title')
                    link = row.find('a')

                    # Get today's and yesterday's date
                    now = datetime.now()
                    today = datetime.today().strftime('%d.%m.%Y.')
                    yesterday = now - timedelta(days=1)
                    yesterday_date = yesterday.strftime('%d.%m.%Y.')

                    # Only add rows that match today's or yesterday's date
                    if publis_data and (publis_data.get_text(strip=True) == today or publis_data.get_text(
                            strip=True) == yesterday_date):
                        all_rows.append((
                            location["blok"],
                            title.get_text(strip=True) if title else 'N/A',
                            price.get_text(strip=True) if price else 'N/A',
                            price_per_m.get_text(strip=True) if price_per_m else 'N/A',
                            f"https://www.halooglasi.com/{link['href']}" if link else 'N/A'

                        ))

            # After all locations have been processed, check if we have any rows and generate the table
            if all_rows:  # If we have valid rows
                cols = ('Blok','Naziv', 'Cena', 'Cena €/m2', 'Link')
                html_table = tabulate(all_rows, headers=cols, tablefmt='html')
                return html_table
            else:
                print("No recent listings found.")
                return 0

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

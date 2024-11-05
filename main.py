import time
import logging
from scrapper import WebScrape
from generate_email import MailService
import re

# Configure logging
logging.basicConfig(level=logging.INFO)

class Main(WebScrape, MailService):
    blokov = ["blok_37", "blok_33", "blok_3", "blok_2", "blok_4"]

    def __init__(self):
        self.test = ""

    def scrape_all_blocks(self):
        for blok in self.blokov:
            try:
                logging.info(f"Scraping block: {blok}")
                scraper = WebScrape(blok)
                content = scraper.web_scraping()
                if re.search(r'\bNaziv\b', content):
                    self.test += f"<br><h3>Stanovi se nalazi u {blok}</h3><br>" + content + "<br>"
                    time.sleep(1)  # Optional: Add delay between requests to avoid rate-limiting
            except Exception as e:
                logging.error(f"Error scraping block {blok}: {e}")

    def send_scraped_content(self):
        self.scrape_all_blocks()
        mail = MailService(self.test)
        mail.send_mail()

if __name__ == "__main__":
    main_object = Main()
    main_object.send_scraped_content()

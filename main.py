import time
import logging
from scrapper_v2 import WebScrape
from generate_email import MailService


# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    LOCATION = [
        {"blok": " Blok 37",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-37"},
        {"blok": " Blok 33",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-33"},
        {"blok": " Blok 3",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-3"},
        {"blok": " Blok 2",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-2"},
        {"blok": " Blok 4",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-4"},
        {"blok": " Blok 5",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-5"},
        {"blok": " Blok 34",
         "link": "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd-novi-beograd-blok-34-carina-studentski-grad"}
    ]
    main_object = WebScrape(LOCATION)
    logging.info("Start scrapping")
    if main_object.scrape_web() !=0:
        mail = MailService(main_object.scrape_web())
        mail.send_mail()
    else:
        logging.info("Nije bilo novih stanova")


Here's a README file based on the Python script you provided. It explains what the script does, how to set it up, and how to run it.

---

# Property Scraper & Email Notifier

This script scrapes property listings from **Halo Oglasi** for specific locations in Belgrade, Serbia, and sends an email notification if new properties are found.

## Features

- Scrapes property listings for specific locations (defined in the script).
- Sends an email notification with the results if new listings are found.
- Logs activity to track the scraping process.

## Dependencies

To run this script, you will need the following Python packages:

- `requests` – for making HTTP requests (likely used within the `WebScrape` class)
- `beautifulsoup4` – for parsing HTML and extracting the required data from the web pages (likely used in `WebScrape`)
- `smtplib` – for sending email notifications (used within `MailService`)
- `logging` – for logging activity (built-in Python library)
  
If you don't have these dependencies installed, you can install them using `pip`:

```bash
pip install requests beautifulsoup4
```

## Setup

1. **Web Scraping Configuration:**
   - The script scrapes listings from **Halo Oglasi** for several locations in Belgrade. The locations are defined in the `LOCATION` list.
   - Each location is defined as a dictionary containing:
     - `blok`: The name of the block/area.
     - `link`: The URL to scrape.

2. **Email Notification:**
   - The `MailService` class is used to send an email notification if new listings are found.
   - The email logic relies on the results returned by the `scrape_web` method of the `WebScrape` class.

3. **Logging:**
   - The script uses Python's built-in `logging` module to log messages at various stages of the scraping process.

## How to Run

### 1. Modify the `LOCATION` List (Optional)

You can modify the `LOCATION` list in the script to add more locations or change the existing ones. Each entry should have the following structure:

```python
{
    "blok": "Location Name",
    "link": "URL of the location page to scrape"
}
```

### 2. Run the Script

Once the configuration is set, you can run the script by executing the following in your terminal:

```bash
python script_name.py
```

This will:
1. Start scraping the property listings from the defined locations.
2. If new listings are found, an email will be sent to the configured address.
3. If no new listings are found, the script will log a message saying "Nije bilo novih stanova" (No new apartments).

### Example Output

If new listings are found, the output will look something like this:

```plaintext
INFO:root:Start scrapping
INFO:root:New apartments found, sending email...
```

If no new listings are found, the output will be:

```plaintext
INFO:root:Start scrapping
INFO:root:Nije bilo novih stanova
```

## Code Walkthrough

### `WebScrape` Class

The `WebScrape` class is responsible for scraping the property listings from the provided URLs. The `scrape_web` method performs the scraping and returns the data or a status code indicating whether any new listings were found.

### `MailService` Class

The `MailService` class handles sending the email notification if new listings are found. It uses the data returned by `scrape_web` to compose the email.

### `Logging`

The script logs the status of the scraping process, including:
- When the scraping starts.
- If new listings are found.
- If no new listings are found.

## Notes

- Make sure to configure your email settings correctly in the `MailService` class.
- The script assumes that the `WebScrape` and `MailService` classes are implemented in separate files (`scrapper_v2.py` and `generate_email.py`, respectively).

## Contributing

Feel free to fork this repository and contribute by creating pull requests. Please ensure that you follow proper coding practices and add tests where applicable.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

This README provides a basic overview of the script and how to set it up and use it. Make sure to update any specific sections (e.g., email configuration, class details) based on your actual implementation in `scrapper_v2.py` and `generate_email.py`.
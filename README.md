# EmailExtractor

A small Python scraper that visits a list of websites and collects the contact email addresses it finds, using Selenium (for JavaScript-rendered pages) and BeautifulSoup with regex matching. Includes a helper to expand shortened URLs.

## Usage

```bash
pip install selenium beautifulsoup4
```

1. Put the target URLs in a `weblinks.csv` file (one URL per row).
2. Run `python EmailScrape.py`. Results are written to CSV.

`URLShortner.py` expands shortened links before scraping.

Please scrape responsibly: respect each site's terms of service and `robots.txt`, and only use the collected addresses in ways that comply with anti-spam and data-protection laws.

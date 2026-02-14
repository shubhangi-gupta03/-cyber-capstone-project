import schedule
import time

from scrapers.advisory_scraper import fetch_advisories
from apis.news_api import fetch_news
from scrapers.helpline_checker import check_helpline_updates

# run every 6 hours
schedule.every(6).hours.do(fetch_advisories)

# run every 12 hours
schedule.every(12).hours.do(fetch_news)

# run daily
schedule.every().day.do(check_helpline_updates)

print("Automation scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)

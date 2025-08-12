import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

WEBHOOK_URL = https://discord.com/api/webhooks/1404934186313318593/Dg1K8XWa0UiT4nfoloJ9A4iHfIctTTpv7FDWOMjw885_KtRTAvrm4Ssn7aegLd1cgda4
URL_MARKETPLACE = https://www.facebook.com/marketplace/oslo/cars?maxPrice=120000&exact=false

def send_to_discord(message):
    requests.post(WEBHOOK_URL, json={"content": message})

def main():
    last_items = set()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        while True:
            page.goto(URL_MARKETPLACE)
            time.sleep(5)
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")
            items = soup.select('a[href*="/marketplace/item/"]')
            current_items = set()
            for item in items:
                link = "https://facebook.com" + item['href'].split("?")[0]
                current_items.add(link)
                if link not in last_items:
                    send_to_discord(f"📢 Nowe ogłoszenie: {link}")
            last_items = current_items
            time.sleep(300)

if __name__ == "__main__":
    main()
Add bot.py

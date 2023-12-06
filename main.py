import requests
from bs4 import BeautifulSoup
import time


def fetch_page(url):
    # Function to fetch the page content with retries
    max_attempts = 5
    for attempt in range(max_attempts):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        time.sleep(2)  # Wait for 2 seconds before retrying
    return None


url = "https://appexchange.salesforce.com/mktcollections/cloud-collections/SalesCloud"
response = fetch_page(url)

if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=lambda href: href and href.startswith(
        'https://appexchange.salesforce.com/appxListingDetail?listingId='))

    for link in links:
        listing_url = link.get('href') + "&tab=r"

        # Fetch the Trailblazer link page with retries
        trailblazer_response = fetch_page(listing_url)

        if trailblazer_response:
            soup_listing = BeautifulSoup(trailblazer_response.content, 'html.parser')

            # Find the trailblazer links using the appropriate selector (update as needed)
            trailblazer_links = soup_listing.select('a[href^="https://trailblazer.me/id="]')

            print("Modified URL:", listing_url)
            for trailblazer_link in trailblazer_links:
                print("Trailblazer URL:", trailblazer_link.get('href'))
        else:
            print("Trailblazer link page not loaded:", listing_url)
else:
    print("AppExchange page not loaded:", url)

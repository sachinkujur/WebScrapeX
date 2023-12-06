import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def find_shadow_element(driver, parent_element, shadow_root_selector):
    # Function to find a shadow DOM element using JavaScript
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", parent_element)
    return shadow_root.find_element(By.CSS_SELECTOR, shadow_root_selector) if shadow_root else None

url = "https://appexchange.salesforce.com/mktcollections/cloud-collections/SalesCloud"
response = fetch_page(url)

if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=lambda href: href and href.startswith('https://appexchange.salesforce.com/appxListingDetail?listingId='))

    # Set up the Selenium web driver (ensure you have the appropriate driver executable and update the path)
    driver = webdriver.Chrome()
    driver.maximize_window()

    for link in links:
        listing_url = link.get('href') + "&tab=r"

        # Load the URL using Selenium
        driver.get(listing_url)

        # Wait for the shadow root element to load
        # shadow_root_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'ul:nth-child(1) > li:nth-child(2) > ace-link:nth-child(1)'))  # Replace
        #     # 'trailblazer-element-id' with the actual ID of the shadow root element
        # )
        #
        # # Find the trailblazer link within the shadow root
        # trailblazer_link = find_shadow_element(driver, shadow_root_element, 'a[href^="https://trailblazer.me/id="]')

        # Find the shadow root of "page-container" using JavaScript
        shadow_root_page_container = driver.execute_script(
            'return document.querySelector("page-container").shadowRoot;')

        # Find the first div inside the shadow root
        first_div = driver.execute_script('return arguments[0].querySelector("div");', shadow_root_page_container)

        # Find the second div inside the first div
        second_div_inside_first_div = driver.execute_script('return arguments[0].querySelector("div:nth-child(2)");',
                                                            first_div)

        # Find all ace-review elements inside the second div
        ace_reviews = driver.execute_script('return arguments[0].querySelectorAll("ace-review");',
                                            second_div_inside_first_div)

        # Access the second ace-review element (assuming it exists)
        target_element = ace_reviews[1]

        print(target_element)

        trailblazer_link = shadow_content.getText()

        if trailblazer_link:
            print("Modified URL:", listing_url)
            print("Trailblazer URL:", trailblazer_link.get_attribute('href'))
        else:
            print("Trailblazer link not found on page:", listing_url)

    # Close the driver after processing all links
    driver.quit()
else:
    print("AppExchange page not loaded:", url)

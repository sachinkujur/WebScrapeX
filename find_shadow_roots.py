from selenium import webdriver

# Set up the Chrome web driver
driver = webdriver.Chrome()

def find_shadow_roots(element):
    # Find the shadow root of the given element using JavaScript
    shadow_root = driver.execute_script('return arguments[0].shadowRoot;', element)

    # If a shadow root is found, print it and search for shadow roots within it
    if shadow_root:
        print("Found a shadow root:", shadow_root)
        find_shadow_roots(shadow_root)

# Navigate to the web page containing the shadow root "page-container"
driver.get('https://appexchange.salesforce.com/appxListingDetail?listingId=a0N300000016a6MEAQ&placement=a0d3u00000B3kbzAAB&tab=r')

# Find the shadow root of "page-container" using JavaScript
page_container = driver.execute_script('return document.querySelector("page-container").shadowRoot;')

# Start searching for shadow roots within the "page-container" shadow root
find_shadow_roots(page_container)

# Close the driver
driver.quit()

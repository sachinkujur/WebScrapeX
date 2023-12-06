import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_salesforce_element():
    url = "https://appexchange.salesforce.com/"

    # Initialize the web driver (make sure to have the appropriate driver installed and added to the PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the URL
    driver.get(url)

    try:
        # Wait for the element to be present
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'analytics-handler > ace-header'))
        # )

        # Execute JavaScript to find and click the element within the Shadow DOM
        js_code = """       
        document.querySelector("#main > page-container").shadowRoot.querySelector("analytics-handler > ace-header").shadowRoot.querySelector("li.appx-context-bar__item.appx-dropdown-trigger.appx-dropdown-trigger-product.appx-dropdown-trigger-with-extra-sub-menu-block > a > span").click();
        """
        driver.execute_script(js_code)
        time.sleep(5)

    except Exception as e:
        print("Error occurred:", e)

    # Close the browser window
        driver.quit()

if __name__ == "__main__":
    click_salesforce_element()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def open_browser(url):
    try:
        # Initialize Chrome WebDriver using webdriver_manager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        # Open the specified URL
        driver.get(url)

        # Add a delay of 5 seconds (you can adjust the time as needed)
        time.sleep(5)
    except Exception as e:
        print("Error occurred while trying to launch the web browser:", e)
    finally:
        # Close the browser after use
        if driver is not None:
            driver.quit()

if __name__ == "__main__":
    # Replace 'https://www.example.com' with the desired URL
    url_to_open = "https://cheqone.atlassian.net/projects/CPT?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.xpandit.plugins.xray__testing-board#!page=test-repository&selectedFolder=64c20e76eec6f8c5e3885892"
    open_browser(url_to_open)
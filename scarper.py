import requests
from bs4 import BeautifulSoup

# The URL of the page to scrape
url = "https://appexchange.salesforce.com/mktcollections/cloud-collections/SalesCloud"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all anchor tags (<a>) with 'href' attribute starting with the specified URL
    links = soup.find_all("a", href=lambda href: href and href.startswith("https://appexchange.salesforce.com/appxListingDetail?listingId="))

    # Process each link and scrape data from the corresponding page
    for link in links:
        # Get the link URL
        link_url = link["href"]

        # Send an HTTP GET request to the link URL
        link_response = requests.get(link_url)

        # Check if the request was successful (status code 200)
        if link_response.status_code == 200:
            # Parse the HTML content using BeautifulSoup for the individual link page
            link_soup = BeautifulSoup(link_response.content, "html.parser")

            # Find the element with the specified <a> tag, 'href' attribute, and 'target' attribute
            target_element = soup.find("a", {"href": "https://trailblazer.me/id/", "target": "_blank"})

            if target_element:
                # Extract and print the content of the element (span inside <a>)
                data = target_element.find("span", {"type-style": "body-2", "class": "bolded"})
                if data:
                    print(data.text.strip())
                else:
                    print("Span element not found inside the <a> tag.")
            else:
                print("Element not found.")

        else:
            print(f"Failed to retrieve the link page. Status code: {link_response.status_code}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

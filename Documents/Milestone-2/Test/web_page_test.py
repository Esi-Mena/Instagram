import requests
from bs4 import BeautifulSoup

# Define the URL of your server
url = "https://instagram-production.up.railway.app"  # Replace with your server's URL

# Define the expected text you want to check for on the web page
expected_text = "Your Expected Text"  # Replace with the text you expect to find

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the text from the page
    page_text = soup.get_text()

    # Check if the expected text is present in the page's content
    if expected_text in page_text:
        print(f"Web page contains the expected text: {expected_text}")
    else:
        print(f"Web page does not contain the expected text: {expected_text}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

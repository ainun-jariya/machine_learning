import requests
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'https://www.lipsum.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing article titles
    article_titles = soup.find_all('h1', class_='')

    # Extract and print the titles
    for title in article_titles:
        print(title.text)
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)

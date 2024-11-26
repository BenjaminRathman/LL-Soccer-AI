import requests  # type: ignore
from bs4 import BeautifulSoup   # type: ignore

# Function to get the HTML content from a URL
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to parse the HTML content using BeautifulSoup
def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')

# Function to extract the name and value using the provided HTML path
def extract_data_one_stock(soup):
    try:
        # Try to extract the <h1> tag from the specific section  # need to work on the find 
        name_tag = soup.find('h1',class_="yf-xxbei9")  #<h1 class="yf-xxbei9">S&amp;P 500 (^GSPC)</h1>
        if name_tag:
            name = name_tag.get_text().strip()
        else:
            print("Name tag not found.")
            name = None

        # Find the value (using the data-field attribute for regular market price)
        value = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
        if value:
            value = value.get_text().strip()
        else:
            print("Value not found.")
            value = None

        return name, value
    except AttributeError as e:
        print(f"Error parsing the content: {e}")
        return None, None

# Main function to scrape Yahoo Finance for a stock/index
def get_content(url):
    html_content = get_html_content(url)
    
    if html_content:
        soup = parse_html(html_content)
        name, value = extract_data_one_stock(soup)
        
       
        
        return [name,value]
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
URL='https://www.amazon.in/product-reviews/B09RG9WPTC'

response = requests.get(URL)
print("response Status code: ", response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
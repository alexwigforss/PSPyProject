from main import test_links
import requests
from bs4 import BeautifulSoup

# requests + beautiful soup

# set url
urlfront = "https://www.impecta.se/sv/froer"
urlpage = "https://www.impecta.se/froer/gronsaker/sommarmorot-nantes-2"

# läs och lagra websidans hela html-kod
front_r = requests.get(urlfront) 
page_r = requests.get(urlpage) 

# läs med web scraper med standard-parser
soup = BeautifulSoup(page_r.content, 'html.parser')

result_link = soup.find(id="Bildkolumn") # för bildlänk. id = "ArtikelNamnfalt" för namn
link_find = result_link.find_all('a')
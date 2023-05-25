from bs4 import BeautifulSoup
import requests

url_start = "https://www.impecta.se"
url_collection = []
url = f"https://www.impecta.se/sv/froer?page=2"
page_html = requests.get(url) 
soup = BeautifulSoup(page_html.text, 'html.parser') 

p = soup.find('span', {'class':"pag-text"})
url_next = p.parent.attrs['href']
url_collection.append(url_start+url_next)
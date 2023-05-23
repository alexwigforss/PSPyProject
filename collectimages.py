#from main import test_links
import requests
from bs4 import BeautifulSoup
from gatherlinks import *

start_url = "https://www.impecta.se"
image_url = {}

def Scrape_picture(article_page):
    url = "NotFound"
# läs in websidans hela html-kod och lagra i soup med standard-parser
    page_html = requests.get(article_page) 
    soup = BeautifulSoup(page_html.text, 'html.parser')
#Hitta rätt plats i koden och dra ut länken
    picture_code = soup.find(id="Bildkolumn") 
    picture_links = picture_code.findAll('a')
    for link in picture_links:
        img = link.attrs['href']
        if "_3.jpg" in img:
            url = start_url+img
            break
    return url

# Hämta artikelsida och artikelnamn ur gatherlinks-samlingen
for key, value in article_pages.items():
    image_url[key] = Scrape_picture(value)
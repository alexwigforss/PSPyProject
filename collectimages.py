# > pip install beautifulsoup4
from main import test_links
import requests
from bs4 import BeautifulSoup

# FÖR ATT HÄMTA BILD-URL FRÅN VARJE SIDA: requests + beautiful soup

start_url = "https://www.impecta.se"
image_url = []
# test-url för en artikelsida
article_page = "https://www.impecta.se/froer/gronsaker/sommarmorot-nantes-2"

# läs in websidans hela html-kod och lagra i soup med standard-parser
page_html = requests.get(article_page) 
soup = BeautifulSoup(page_html.text, 'html.parser')

def scrape_picture():
    picture_code = soup.find(id="Bildkolumn") 
    picture_links = picture_code.findAll('a')
    for link in picture_links:
        img = link.attrs['href']
        if "_3.jpg" in img:
            url = start_url+img
            print(url)
            image_url.append(url)

scrape_picture()

def scrape_name():
    text_code = soup.find(id="Faktakolumn")
    name_tag = text_code.find('h1') #tag: <h1, attrs: id="", ignorera: <br-span> (innehållet skrivs ut genom .text)
    print("name_code: " + str(name_tag))
    name_str = str(name_tag.text)
    print("name_str: " + name_str)

scrape_name()

#<a rev="/img/bilder/artiklar/zoom/89001_3.jpg?constrain=1&amp;w=850&amp;m=1651481439" OK as is
#<a href="/bilder/artiklar/zoom/89001_3.jpg?m=1651481439" OK as is
#from main import test_links
import requests
from bs4 import BeautifulSoup
#from gatherlinks import *

if __name__ == "__main__":

    def Scrape_picture(article_page):
        start_url = "https://www.impecta.se"
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
    def Get_article(article_pages):
        image_url = {}
        for key, value in article_pages.items():
            image_url[key] = Scrape_picture(value)
        return image_url



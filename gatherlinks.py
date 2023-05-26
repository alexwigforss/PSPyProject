import requests
from bs4 import BeautifulSoup

def Get_fifty_articles(soup, start_url, article_pages):
    # Sorterar ut de 50 första artiklarna på översikssidan ( för att undvika dubbletter ur övriga erbjudanden på sidan)
    text_code = soup.findAll('h2', limit=50)
    for i in text_code:
        name = i.contents[1].text
        url = start_url+i.contents[1].attrs['href']
        article_pages[name] = url

def Crawl_frontpages():
# Läs in första översiktssidan på hemsidan
    start_url = "https://www.impecta.se"
    startpage = "/sv/froer?page=1"
    url = start_url+startpage
    article_pages = {}
    while(True):
        try: 
            page_html = requests.get(url) 
            soup = BeautifulSoup(page_html.text, 'html.parser')
        # Med html-soupkoden för aktuell översiktssida skrapas adresserna till alla 50 artiklar
            Get_fifty_articles(soup,start_url, article_pages)
        # Kollar om översiktssidan har en "Nästa"-knapp, hämtar url till nästa sida
            p = soup.find('span', {'class':"pag-text"})
            url_next = p.parent.attrs['href']
        # Går till nästa översiktssida, för ny loop
            url = start_url+url_next
        except AttributeError:
            return article_pages

if __name__ == "__main__":
    Crawl_frontpages()
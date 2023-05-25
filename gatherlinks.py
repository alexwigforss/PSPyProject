import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    start_url = "https://www.impecta.se"
    startpage = "/sv/froer?page=1"
    article_pages = {}

    # läs in websidans hela html-kod och lagra i soup med standard-parser
    page_html = requests.get(start_url+startpage) 
    soup2 = BeautifulSoup(page_html.text, 'html.parser')

    def Get_fifty_pages(soup=soup2):
        # Sorterar ut de 50 första artiklarna på översikssidan ( för att undvika dubbletter ur övriga erbjudanden på sidan)
        text_code = soup.findAll('h2', limit=50)
        for i in text_code:
            name = i.contents[1].text
            url = start_url+i.contents[1].attrs['href']
            article_pages[name] = url
            print(url)
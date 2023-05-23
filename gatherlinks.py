import requests
from bs4 import BeautifulSoup

start_url = "https://www.impecta.se"
startpage = "/sv/froer?page=1"
article_pages = []

# läs in websidans hela html-kod och lagra i soup med standard-parser
page_html = requests.get(start_url+startpage) 
soup = BeautifulSoup(page_html.text, 'html.parser')

# <div class="PT_Wrapper  test1-2"> / <div class="box bottom-xs"> / <div class="PT_lower"> / <div class="PT_Faktaruta"> /	<h2 class="PT_Beskr row-margin-bottom-small hoveropacity"> / <a href="/froer/gronsaker/spenat-f1-samos">
def from_name():
    text_code = soup.findAll('h2')
    for i in range(50):
        url = start_url+text_code[i].contents[1].attrs['href']
        article_pages.append(url)

from_name()

print(article_pages)

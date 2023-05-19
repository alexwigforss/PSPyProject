import requests
from bs4 import BeautifulSoup

page_nr=1
# scraper kan med hjälp av loop läsa url för varje sida 1-37:
url = "https://www.impecta.se/sv/froer?page="+str(page_nr) 

#spara HTML från sida
page_code = requests.get(url)

#Skriv som ren text
clean_code = page_code.text
page_code = page_code.content #alt
#Skapa ett BS-objekt med koden i
soup = BeautifulSoup(clean_code, features="html.parser")
soup2 = BeautifulSoup(page_code, 'html.parser') #alt

#Sortera ut alla länkar (key = 'a') eller headers (t.ex 'h2')
for item in soup.findAll('a'):
    pass#print(item)

#Sortera ut knappar som leder till angränsande sida, efter specifika attribut ('class', 'id', 'href') bland länkar
for item in soup.findAll('a', {'class': "pag-text"}):
    pass #print (item)

#Sortera ut alla länkar som leder till frösida
for item in soup.findAll('h2').find('a', attrs={'class': 'pag-text'}):
    pass#print (item)

# crawler kan 1. scrolla ner och trycka 'visa mer' tills knappen inte finns längre, sedan läsa av hela sidan
#           eller 2. läsa en sida, trycka 'nästa' tills knappen inte finns längre

# HTML för "nästa"-knappen ( if class="pag-text" != "Nästa"):
next_btn = ['<a href="/sv/froer?page=37" rel="nofollow">',
'<span class="pag-text">Nästa</span>',
'<span class="pag-icon">»</span>',
'</a>']
# HTML för att hämta namnet på varje växt-sida:
name_html = ['<h1 id="ArtikelnamnFalt"', 'itemprop="name"', 'class="span_12_of_12">', "Väderspåman 'Tetra Polar Star'</h1>"]

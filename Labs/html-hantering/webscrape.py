from webcrawl import *

url_start = "https://www.impecta.se"
url_page = []

code_main = soup.find('main')
code_headers = code_main.findAll('h2')

h2 = []
i=0
while i < 50:
 h2.append(code_headers[i])
 i+=1

#i varje header, hitta länktyp ('a') med attributet 'href'
h2[0].find('a').attrs['href']

while len(url_page) < 50:
    url_page.append(code_headers[i].find('a').attrs['href'])


# KÄLLA: https://www.youtube.com/watch?v=MH3641s3Roc : Pythonology - "Web Scraping to CSV | Multiple Pages Scraping with Beautiful Soup"

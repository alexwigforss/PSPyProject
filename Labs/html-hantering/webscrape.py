# > pip install Scrapy
from webcrawl import *

url_start = "https://www.impecta.se"
url_page = []
urlfront = "https://www.impecta.se/sv/froer"

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


# KÄLLA (inspiration): https://www.youtube.com/watch?v=MH3641s3Roc : Pythonology - "Web Scraping to CSV | Multiple Pages Scraping with Beautiful Soup"


    #front_r = requests.get(urlfront) 

# Kodexempel på iterator från 
# https://www.octoparse.com/blog/build-web-crawler-with-python
'''
# td in HTML is 'table data'
data_iterator = iter(soup.find_all('td'))
# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
while True:
try:
country = next(data_iterator).text
confirmed = next(data_iterator).text
deaths = next(data_iterator).text
continent = next(data_iterator).text
data.append((
country,
confirmed,
deaths,
continent
))
# StopIteration exception is raised when
# there are no more elements left to
# iterate through
except StopIteration:
break
# Sort the data by the number of confirmed cases
data.sort(key = lambda row: row[1], reverse = True)
'''

# På hemsidan, copy inner html tar endast koden under/innanför den markerade raden
# copy outer HTML inkluderar den markerade raden
'''<a href="/sv/froer?page=2" rel="nofollow">
<span class="pag-text">Nästa</span>
<span class="pag-icon">»</span>
</a>'''
from bs4 import BeautifulSoup
import requests
import gatherlinks

if __name__ == "__main__":
    def Crawl_frontpage(url_front = "https://www.impecta.se/sv/froer"):
        url_start = "https://www.impecta.se"
    # Läs in första översiktssidan på hemsidan
        url = url_front
        while(True):
            try: 
                page_html2 = requests.get(url) 
                soup = BeautifulSoup(page_html2.text, 'html.parser')
            # Med html-soupkoden för aktuell översiktssida skrapas adresserna till alla 50 artiklar
                gatherlinks.Get_fifty_pages(soup)
            # Kollar om översiktssidan har en "Nästa"-knapp, hämtar url till nästa sida
                p = soup.find('span', {'class':"pag-text"})
                url_next = p.parent.attrs['href']
            # Går till nästa översiktssida, för ny loop
                url = url_start+url_next
            except AttributeError:
                break
    # pass arg limit=50 in find()
    '''
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



# Kodexempel på iterator från 
# https://www.octoparse.com/blog/build-web-crawler-with-python

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
# I projektdefinition:
    - namn + mail
    - vad för sorts program (1-2 meningar)
    - Valda bibliotek + länk till dokumentationen
    - ev länk till kod som projektet ska bygga ut
    - länk till git-repo

## Inlämning:
    - git-historik
    - referenser till lånad kod och information
    - slideshow för presentation
    - video eller bilder över utvecklingsprocessen

## Att göra:
Minna:
    - Web crawler som hämtar alla länkar till fröernas sidor från impecta.se
    - Web scraper som hämtar bilder på fröpåsens baksida (i url-format) från varje länk (om bildadressen innehåller "_3.jpg"), samt det svenska namnet
    - Lagrar växtnamn + bild-url i en dictionary
   
Alexander:
    - Ladda ner bilderna från bild-url-dictionaryt
    - Script för att läsa av text från bilderna
    - Ignorera överflödig text och lagra information om:
        Plantnamn (finns som key i dictionaryt)
        Radavstånd (y)
        Plantavstånd (x)
            Medelavstånd (initialisers som -1)
        Såtid
        Skördetid
    Senare alternativ:
        Portionsmängd
        Perenn/ettårig
        (Grotid)
        (Grobarhet)
    - Grundbearbetning av grafritandet: antal och placering
   
Båda:
    - Metod som räknar ut varje plantas Medelavstånd (av x och y), för scatter-sådd (ojämn distribution)

    - Programkörning som tar emot: odlingsyta (x och y), plantnamn, fördelning i procent per plantsort, jämn distribution (on/off)

    - Funktion som beräknar överlapp baserat på NÄR de olika fröerna ska planteras/skördas
   
    - Funktion som tar de plantor som har ett odlingsöverlapp och räknar ut ANTAL frö per sort, baserat på: fröutrymme, odlingsyta, fördelning

    - Skriv ut grafer månad för månad som ritar ut placering (i scatter eller rader) och skörd av fröer (Fröet byter färg när det är skördeklart?)


    https://docs.google.com/document/d/1fEIx-ZkkdTSlERRcq6IuiG00gp1I6G9e03dvIhDI4Kw/edit?usp=sharing

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
    - Web crawler som hämtar alla länkar till fröer från impecta.se
    - Web scraper hämtar bilder från varje länk (om bildadressen innehåller "_3.jpg"), samt det svenska namnet
    
    - Open-cv script för att läsa av text från bildlänkarna
    - Varje planta ska lagra information om: 
        Plantnamn (artnamn, sortnamn)
        Radavstånd (y)
        Plantavstånd (x)
            Medelavstånd
        Såtid
        Skördetid 
    Senare alternativ: 
        Portionsmängd
        Perenn/ettårig
        (Grotid)
        (Grobarhet)
    
    - Programkörning som tar emot: odlingsyta (x och y), plantnamn, fördelning i procent per plantsort, jämn distribution (on/off)

    - Funktion som beräknar överlapp baserat på när de olika fröerna ska planteras/skördas
    
    - Funktion som tar de plantor som har ett odlingsöverlapp och räknar ut antal frö per sort, baserat på: fröutrymme, odlingsyta, fördelning

    - Skriv ur grafer månad för månad som ritar ut placering och skörd av fröer
    - Fröet byter färg när det är skördeklart?
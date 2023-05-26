# > pip install beautifulsoup4
# > pip install opencv-python
# > pip install numpy
# > pip install matplotlib
# > pip install pytesseract

import plantclass
import calculations
import gatherlinks
import collectimages

#Byt ur mot image_urls
test_images = {"Slanggurka 'Beth Alpha'": "https://www.impecta.se/bilder/artiklar/zoom/9145_3.jpg", 
               "Höstmorot 'De Saint-Valery'": "https://www.impecta.se/bilder/artiklar/zoom/9396_3.jpg", 
               "Gråsockerärt 'Lokförare Bergfälts Jätteärt'":"https://www.impecta.se/bilder/artiklar/zoom/10221_3.jpg", 
               "Kålrot 'Champion'":"https://www.impecta.se/bilder/artiklar/zoom/92201_3.jpg",
               "Honungsmelon 'Honey Dew'": "https://www.impecta.se/bilder/artiklar/zoom/93601_3.jpg"}

test_links = ["https://www.impecta.se/froer/gronsaker/honungsmelon-honey-dew", 
              "https://www.impecta.se/froer/gronsaker/grasockerart-_lokforare-bergfalts-jatteart_",
              "https://www.impecta.se/froer/gronsaker/hostmorot-st-valery",
              "https://www.impecta.se/froer/gronsaker/jattelok-ailsa-craig",
              "https://www.impecta.se/froer/gronsaker/kalrot-champion"]


def Try_name():
    while(True):
        name_input = str(input("Växtens namn: "))
        name_exists = []
        for plant in plantclass.Test_Database:			#TODO: byt till faktiska listan
            if name_input.lower() in plant.name.lower():
                name_exists.append(plant)
        if len(name_exists) == 1:
            print(f"Du har valt {str(name_exists[0].name)}")
            return name_exists[0]
        elif len(name_exists) == 0: 
            print("Växten är inte tillgänglig, försök med ett annat namn.")
            continue
        elif len(name_exists) > 1:
            print(f"Hittade flera liknande alternativ: ")
            for i in name_exists:
                    print("    ", i.name)
            print("Vilket menade du?")
            continue
    
def Try_percentage(percent, plant):    
    while(True):
        try:
            amount = float(input(f"Andel plantor av {plant.name} du vill sätta i procent: "))
            if(percent-amount < 0):
                raise Exception("Du kan inte odla mer än 100 procent.")
        except Exception as e:
            print(e, f"Du har {percent}% kvar att fördela")
            continue
        else:
            return amount

def Set_land():
    print("~~~ Välkommen till planterings-planeraren ~~~")      #TODO exception handling, fel input
    land_x = float(input("Hur stort utrymme har du att odla på? \nLängd (cm): "))
    land_y = float(input("Djup (cm): "))
    land_name = input("Namnge odlingslandet: ")
    return plantclass.Land(land_name, land_x, land_y)

def Choose_plants(Try_name, Try_percentage):
    to_plant = []
    print("Nu ska du få ange vilka sorts växter du vill odla och hur mycket av varje sort i procent")
    percent = 100
    while(percent > 0):
        #Ange ett plantnamn:
        plant = Try_name() 
        #Ange procentandelen:
        percentage = Try_percentage(percent, plant)
        to_plant.append([plant, percentage])
        #Fortsätt loop om det finns plats för fler växter
        percent -= percentage
        if(percent == 0): 
            return to_plant
        else:
            print(f"Du har angett {100-percent}% av årets odlingar. Ange nästa planta.")

def Set_distribution():
    print("Nu ska du få välja om du vill plantera dina växter i rader eller med spridd sådd")
    while(True):
        dist_ans = input("Ange 'r' för rad-sådd, och 's' för spridd sådd: ").lower()
        if (dist_ans == 'r'):
            return True
        elif(dist_ans == 's'):
            return False
        else: continue

if __name__ == '__main__':
    import printgraph as pg
    ans = input("Ladda ner databasen? (y / n): ")
    if ans.lower() == "y":
        article_pages = gatherlinks.Crawl_frontpages("https://www.impecta.se/sv/froer?page=1")
        image_urls = collectimages(article_pages)
    else: image_urls = test_images
    # Odlingsutrymme
    growing_area = Set_land()
    # Växter och andel
    chosen_plants = Choose_plants(Try_name, Try_percentage) #[Plant-object, procentmängd]
    # Fördelningssätt
    distribution_row = Set_distribution()
    # Gör beräkningar för fröer
    nr_of_seeds = calculations.NumberOfSeeds(chosen_plants, growing_area)
    print(f"growingarea: {growing_area.__dict__}") 
    for each in chosen_plants:
        print(f"plant: {each[0].__dict__}")
    pg.assembleLand(growing_area, chosen_plants, distribution_row)

    # TODO escape-button för att avbryta programmet?    
'''
    growing_area = plantclass.Land("test", 200, 300)
    plant1 = plantclass.Plant('gurka', 20, 30, 6, 10)
    plant2=plantclass.Plant('morot', 4, 30,  6, 9)
    chosen_plants = [[plant1, 60], [plant2, 40]] # procent
    nr_of_seeds = [[plant1, 15], [plant2, 171]]   # antal
    distribution_row = False
    pg.assembleLand(growing_area, chosen_plants, distribution_row)
'''    
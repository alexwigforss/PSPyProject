# > pip install beautifulsoup4
# > pip install opencv-python
# > pip install numpy

from plantclass import Land
import calculations

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
        for name in test_images.keys():			#TODO: byt till faktiska listan
            if name_input.lower() in name.lower():
                name_exists.append(name)
        if len(name_exists) == 1:
            print(f"Du har valt {name_exists[0]}")
            return name_exists[0]
        elif len(name_exists) == 0: 
            print("Växten är inte tillgänglig, försök med ett annat namn.")
            continue
        elif len(name_exists) > 1:
            print(f"Hittade flera liknande alternativ: ")
            for i in name_exists:
                    print("    ", i)
            print("Vilket menade du?")
            continue
    
def Try_percentage(percent, plant):    
    while(True):
        try:
            amount = float(input(f"Andel plantor av {plant} du vill sätta i procent: "))
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
    land_y = float(input("Bredd (cm): "))
    land_name = input("Namnge odlingslandet: ")
    growing_area = Land(land_name, land_x, land_y)
    return growing_area

def Choose_plants(Try_name, Try_percentage):
    to_plant = []
    print("Nu ska du få ange vilka sorts växter du vill odla och hur mycket av varje sort i procent")
    percent = 100
    while(percent > 0):
        #Ange ett plantnamn:
        plant = Try_name() 
        #Ange procentandelen:
        amount = Try_percentage(percent, plant)
        to_plant.append([plant, amount])
        #Fortsätt loop om det finns plats för fler växter
        percent -= amount
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
            break
        elif(dist_ans == 's'):
            return False
            break
        else: continue

if __name__ == '__main__':
    import printgraph as pg
    # Odlingsutrymme
    growing_area = Set_land()
    # Växter och andel
    chosen_plants = Choose_plants(Try_name, Try_percentage)
    # Fördelningssätt
    distribution_row = False #activate later: Set_distribution()
    # Gör beräkningar för fröer
    nr_of_seeds = calculations.NumberOfSeeds(chosen_plants, growing_area)
    # {'name': 'morot', 'x': 4, 'y': 3, 'plant_month': 6, 'harvest_month': 9, 'mid_dist': 3.5, 'row_space': 12, 'scatter_space': 12.25}
    pg.assembleLand(growing_area, chosen_plants, percent_list):




    # TODO escape-button för att avbryta programmet?    

    
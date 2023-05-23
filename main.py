# > pip install beautifulsoup4
# > pip install opencv-python


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

if __name__ == '__main__':
    # Input från användaren:
    to_plant = []
    land_area = 0
    distribution_row = False
                                                                # TODO escape-button för att avbryta programmet?
    # Odlingsutrymme
    print("~~~ Välkommen till planterings-planeraren ~~~")      #TODO exception handling, fel input
    land_x = float(input("Hur stort utrymme har du att odla på? \nLängd: "))
    land_y = float(input("Bredd: "))
    land_area = land_x * land_y
    
    # Växter och andel
    print("Nu ska du få ange vilka sorts växter du vill odla och hur mycket av varje sort i procent")
    percent = 100
    while(percent > 0):
        #Ange ett plantnamn:
        plant = Try_name() 
        #Ange procentandelen:
        amount = Try_percentage(percent, plant)
        to_plant.append([plant, amount])
        #Fortsätt loop
        percent -= amount
        if(percent == 0): break
        print(f"Du har angett {100-percent}% av årets odlingar. Ange nästa planta.")
    
    # Fördelningssätt
    print("Nu ska du få välja om du vill plantera dina växter i rader eller med spridd sådd")
    while(True):
        dist_ans = input("Ange 'r' för rad-sådd, och 's' för spridd sådd: ").lower()
        if (dist_ans == 'r'):
            distribution_row = True
            break
        elif(dist_ans == 's'):
            distrubution_row = False
            break
        else: continue
    
    print("\nDu planterar: ")
    for i in to_plant:
        print(f"    {i[1]}%  {i[0]}")
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

# Odlingsutrymme
print("~~~ Välkommen till planterings-planeraren ~~~")
land_x = float(input("Hur stort utrymme har du att odla på? \nLängd: "))
land_y = float(input("Bredd: "))
land_area = land_x * land_y

# Växter och andel
print("Nu ska du få ange vilka sorts växter du vill odla och hur mycket av varje sort i procent")
to_plant = []
percent = 100
while(percent > 0):
    plant = str(input("Växtens namn: "))
    amount = float(input(f"Andel plantor av {plant} du vill sätta i procent: "))
    if(percent-amount < 0):
        print(f"Du kan inte odla mer än 100 procent. Du har {percent}% kvar att fördela")
        continue
    else:
        percent -= amount
        to_plant.append({plant: amount})
    if(percent == 0): break
    print(f"Du har angett {100-percent}% av årets odlingar. Ange nästa planta.")

# Fördelningssätt
distribution_row = False
print("Nu ska du få välja om du vill plantera dina växter i rader eller med spridd sådd")
while(True):
    dist_ans = input("Ange 'r' för rad-sådd, och 's' för spridd sådd").lower()
    if (dist_ans == 'r'):
        distribution_row = True
        break
    elif(dist_ans == 's'):
        distrubution_row = False
        break
    else: continue
    
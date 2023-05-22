from plantclass import *

TEST_to_plant = [["morot", 40], ["gurka", 60]]
TEST_land_area = 4*5
distribution_row = False

used_area = 0
# Funktion som räknar ut antal frö per sort, baserat på: fröutrymme(medelavstånd), odlingsyta, fördelning i procent
for item in TEST_to_plant:
    for plant in TestPlants:
        seed = 0
        if item[0] in plant.name:
            seed = plant
            break
    if seed == 0: print("Valda växten finns inte i fröbasen")
    #Skriv om räknetal
    percent = item[1]/100
    land_in_cm2 = TEST_land_area*10000
    #Frön som får plats på hela tillgängliga arean
    seed_per_land =  land_in_cm2 / seed.scatter_space		
    #Antalet beräknas på fördelning i procent
    number_of_seeds = percent * seed_per_land 		
    int_seed_number = int(number_of_seeds)
    
#För felsökning/kontroll: utrymme per frö, fördelning vid avrundning etc
    seed_area = number_of_seeds * seed.scatter_space
    int_seed_area = int(int_seed_number * seed.scatter_space)
    used_area+=int_seed_area
    print(f"\n{seed.name}, antal frön: {int_seed_number} ({number_of_seeds})\n   utrymme dessa frön tar: {int_seed_area} ({seed_area}) cm2")
print(f"\nTotalt används {used_area/10000} av {TEST_land_area} kvm")

from plantclass import *

TEST_to_plant = [["morot", 40], ["gurka", 60]]
TEST_land_area = 4*5
distribution_row = False

# Funktion som räknar ut antal frö per sort, baserat på: fröutrymme(medelavstånd), odlingsyta, fördelning i procent
def GetNumberOfSeeds(item, land_area):
# Hämta info om den angivna växten ur databasen
    seed = 0
    for plant in TestPlants:
        if item[0] in plant.name:
            seed = plant
            break
    if seed == 0: 
        print("Valda växten finns inte i fröbasen")
        return 0
#Skriv om räknetal
    percent = item[1]/100
    land_in_cm2 = TEST_land_area*10000
#Frön som får plats på hela tillgängliga arean
    seed_per_land =  land_in_cm2 / seed.scatter_space		#TODO Gör funktion för rad-sådd
#Antalet beräknas på fördelning i procent
    number_of_seeds = percent * seed_per_land 		
    int_seed_number = int(number_of_seeds)

    return int_seed_number
'''#För felsökning/kontroll: utrymme per frö, fördelning vid avrundning etc
    used_area = 0
    seed_area = number_of_seeds * seed.scatter_space
    int_seed_area = int(int_seed_number * seed.scatter_space)
    used_area+=int_seed_area
    print(f"\n{seed.name}, antal frön: {int_seed_number} ({number_of_seeds})\n   utrymme dessa frön tar: {int_seed_area} ({seed_area}) cm2")
    print(f"\nTotalt används {used_area/10000} av {TEST_land_area} kvm")'''

# Lagra namn och antal frö av valda sorter i en dict
def NumberOfSeeds(chosen_plants, land_area):
    nr_of_seeds = {}
    for item in chosen_plants:
        nr_of_seeds[item[0]] = GetNumberOfSeeds(item, land_area)    
    return nr_of_seeds

print("Totalt behövs:", NumberOfSeeds(TEST_to_plant, TEST_land_area), "frön.")


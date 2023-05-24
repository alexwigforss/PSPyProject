from plantclass import *

TEST_to_plant = [["morot", 40], ["gurka", 60]]
TEST_land_area = 80*120
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
    land_in_cm2 = TEST_land_area
#Frön som får plats på hela tillgängliga arean
    seed_per_land = land_in_cm2 / seed.mid_dist*seed.mid_dist		#TODO Gör funktion för rad-sådd
#Antalet beräknas på fördelning i procent
    number_of_seeds = percent * seed_per_land 		
    int_seed_number = int(number_of_seeds)

    return int_seed_number

# Lagra namn och antal frö av valda sorter i en dict key=växtnamn, value=antal frön
def NumberOfSeeds(chosen_plants, land_area):
    nr_of_seeds = {}
    for item in chosen_plants:
        nr_of_seeds[item[0]] = GetNumberOfSeeds(item, land_area)    
    return nr_of_seeds

print("Totalt behövs:", NumberOfSeeds(TEST_to_plant, TEST_land_area), "frön.")


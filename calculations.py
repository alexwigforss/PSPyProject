import plantclass

TEST_to_plant = [["morot", 40], ["gurka", 60]]
TEST_land_area = 80*120
distribution_row = False

# Funktion som räknar ut antal frö per sort, baserat på: fröutrymme(medelavstånd), odlingsyta, fördelning i procent
def GetNumberOfSeeds(item, growing_area):
#Skriv om räknetal
    print(f"item[0]: {item[0].__dict__}\n item[1]: {item[1]}")
    percent = item[1]/100 #0.4
    print("procentandel: ", percent)
    land_area = growing_area.width * growing_area.height
    print("land_area: ", land_area)
#Frön som får plats på hela tillgängliga arean
    seed_per_land = land_area / (item[0].mid_dist*item[0].mid_dist)		#TODO Gör funktion för rad-sådd
    print("seedPerLand: ", seed_per_land)
#Antalet beräknas på fördelning i procent
    number_of_seeds = percent * seed_per_land 		
    print("nr of seeds: ",number_of_seeds)
    int_seed_number = int(number_of_seeds)
    print("int_seed_nr: ",int_seed_number, item[0].name)
    return int_seed_number

# Lagra namn och antal frö av valda sorter i en dict key=växtnamn, value=antal frön
def NumberOfSeeds(chosen_plants, growing_area):
    nr_of_seeds = []
    for item in chosen_plants:
        nr_of_seeds.append([item[0], GetNumberOfSeeds(item, growing_area), item[1]/100])    
    return nr_of_seeds # Returnerar förhoppningsvis lista med list[Plant(växtens objekt), antalFrön]

#Returnera del av range
def num_to_range(num, inMin, inMax, outMin, outMax):
    result = outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin))
    print(result)
    return result
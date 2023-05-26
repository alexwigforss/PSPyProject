import plantclass

TEST_to_plant = [["morot", 40], ["gurka", 60]]
TEST_land_area = 80*120
distribution_row = False

def Get_plant_space(plant, growing_area, row):
    if row:
        x = plant.x
        y = plant.y
    else:
        x = plant.mid_dist
        y = plant.mid_dist
    number_of_seeds = GetNumberOfSeeds(plant[0], plant[1, growing_area])
    seed_occupation_in_x = x * number_of_seeds
    seed_occupation_in_y = y * number_of_seeds
    x_in_percent = seed_occupation_in_x / growing_area.width
    y_in_percent = seed_occupation_in_y / growing_area.height
    return {'seeds_in_x':seed_occupation_in_x, 'seeds_in_y': seed_occupation_in_y, 'seed_percent_of_xspace':x_in_percent,'seed_percent_of_yspace':y_in_percent}

def GetNumberOfSeeds(plant, percentage, growing_area, row): #med distribution_rows = False
#Skriv om räknetal
    percent = percentage/100 #0.4
#Antal beräknas på X och Y oavsett dist_row
    if row:
      x = plant.x
      y = plant.y
    else: 
      x, y = plant.mid_dist
    seed_per_x = (growing_area.width / x) * percent
    seed_per_y = (growing_area.height / y) * percent
    number_of_seeds = seed_per_x * seed_per_y
    return int(number_of_seeds)
    
# Funktion som räknar ut antal frö per sort, baserat på: fröutrymme(medelavstånd), odlingsyta, fördelning i procent
def GetNumberOfSeeds(item, growing_area):
#Skriv om räknetal
    percent = item[1]/100 #0.4
    land_area = growing_area.width * growing_area.height
#Frön som får plats på hela tillgängliga arean
    seed_per_land = land_area / (item[0].mid_dist*item[0].mid_dist)		#TODO Gör funktion för rad-sådd
#Antalet beräknas på fördelning i procent
    number_of_seeds = percent * seed_per_land 		
    int_seed_number = int(number_of_seeds)
    #print(f"item[0]: {item[0].name}\n item[1]: {item[1]}, procentandel: {percent}, land_area: {land_area}, seedPerLand: {seed_per_land}, nr of seeds: {number_of_seeds}, int_seed_nr: {int_seed_number}")
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
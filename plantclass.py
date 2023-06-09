class Plant:    
    def __init__(self, name, x_dist_cm, y_row_cm, plant_month, harvest_month):
        self.name = name
        self.x = x_dist_cm
        self.y = y_row_cm
        self.plant_month = plant_month
        self.harvest_month = harvest_month
    # Area för radavstånd resp spridd sådd:
        self.mid_dist = (self.x + self.y) / 2
        self.row_space = self.x * self.y
        self.scatter_space = ((self.x + self.y) / 2) * ((self.x + self.y) / 2)

# Importera dessa för att experimentera med matplotlib:
#                Plant(namn,radavst,plantavst,såmånad,skördemånad)
Test_Database = [Plant("morot", 30, 40, 6, 9),
                 Plant("gurka", 20, 30, 6, 10),
                 Plant("melon", 50, 50, 6, 10),
                 Plant("kålrot", 20, 50, 6, 10)]
INDEX = 0
class Land:
    def __init__(self, label, width,height): # width = x, height=y
        global INDEX
        self.index = INDEX
        INDEX +=1
        self.label = str(label)
        self.width = float(width)
        self.height = float(height)
TestLand = Land('grönsakslandet',80,120)
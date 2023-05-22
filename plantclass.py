# klass för varje frösort med: 
#       Plantnamn (finns som key i dictionaryt)
#        Radavstånd (y)
 #       Plantavstånd (x)
  #      Medelavstånd
   #     Såtid (första)
    #    Skördetid (dagar)
#    Senare alternativ:
 #       Portionsmängd
  #      Perenn/ettårig
   #     (Grotid)
    #    (Grobarhet)

class Plant:    
    def __init__(self, name, x, y, plant_month, growth_days):
        self.name = name
        self.x = x
        self.y = y
        self.plant_month = plant_month
        self.growth_time = growth_days
    # Area för radavstånd resp spridd sådd:
        self.row_space = self.x * self.y
        self.scatter_space = ((self.x + self.y) / 2) * ((self.x + self.y) / 2)

# Importera dessa för att experimentera med matplotlib:
TestPlant = Plant("morot", 4, 6, 6, 30)
TestPlant2 = Plant("gurka", 2, 4, 6, 60)
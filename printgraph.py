# Skriv ut grafer månad för månad som ritar ut placering (utgå från spridd sådd) av rätt antal fröer, och när de ska skördas

# Hitta frö med tidigast sådd, [rita ut rätt antal av fröet i grafen]

# [Hitta nästa frö-sådd, rita ut rätt antal]

# markera skördetid 

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
# from plantclass import TestLand as tl

# plt.ion()
class LandAnimation:
    def __init__(self, land = '', plants=[],percent=[],rowdist=True):
        self.land = land
        self.qoute = len(plants)
        # print('qoute = ', self.qoute)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(0, 0)
        self.plants = plants
        self.percent=percent
        self.ListOfPlants = []
        L_INDEX = 0
        for each in plants:
            if rowdist:
                YSPACE = plants[L_INDEX].y
                XSPACE = plants[L_INDEX].x
            elif not rowdist:
                YSPACE = plants[L_INDEX].mid_dist
                XSPACE = plants[L_INDEX].mid_dist
                # width = x = hori, height=y=vert
            nr_of_hori=int(land.width/XSPACE) # rows
            nr_of_vert=int(land.height/YSPACE/self.qoute) # cols
            #nr_of_vert=int(land.height/YSPACE*self.percent[L_INDEX]) # cols
            
            #print('nr_of_vert ',nr_of_vert)
            #print('YSpace: ' , YSPACE,'XSpace: ' , XSPACE)

            Y_START = land.height/self.qoute*L_INDEX
            y = np.full((nr_of_hori, nr_of_vert), 0)
            for each in y:
                each[:] = np.arange(Y_START + YSPACE/2, Y_START + YSPACE*nr_of_vert+(YSPACE/2), YSPACE, dtype=float)
# width = x = hori, height=y=vert
            x = np.full((nr_of_hori, nr_of_vert), 0)
            i = 1
            for each in x:
                each[:]=XSPACE*i-XSPACE/2
                i+=1
            s = np.full((nr_of_hori, nr_of_vert), 1000)
            self.ListOfPlants.append(plt.scatter(y,x,s=s,label = plants[L_INDEX].name))
            L_INDEX += 1
        
        # https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
        # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
        self.legend = plt.legend(bbox_to_anchor =(0.25, 1.15), ncol = 2)
        # https://www.w3schools.com/python/matplotlib_labels.asp
        self.title = plt.title(land.label)
        # https://datavizpyr.com/how-to-draw-a-rectangle-on-a-plot-in-matplotlib/
        # https://www.statology.org/matplotlib-rectangle/
        self.ax.add_patch(plt.Rectangle((0, 0), self.land.height, self.land.width, fill = False),)

    def Calculate_plant_area(self, growing_area_y, number_of_seeds,plant):
        seed_occupation_in_y = plant.mid_dist * number_of_seeds
        occupation_in_percent = seed_occupation_in_y / growing_area_y
        return occupation_in_percent

    def animate(self,frame_nr): # a.k.a update
        q = 0
        for each in self.ListOfPlants:
            if frame_nr < (self.plants[q].x)*20:
                # https://www.digitalocean.com/community/tutorials/numpy-ones-in-python
                each.set_sizes(np.ones(self.qoute)*frame_nr)
            q += 1
        tup = self.line,self.title
        # https://datagy.io/python-append-to-tuple/
        for each in self.ListOfPlants:
            tup = tup + (each,)
        return tup

def assembleLand(land, complete_list, rowdist): #complete_list innehåller [ [PlantObjekt, int(antal_fröer)], [PlantObjekt, int(antal_ fröer)] ]
    plant= []
    percent=[]
    occupation_in_percent = []
    for each_plant in complete_list:
        plant.append(each_plant[0])
        percent.append(each_plant[1]/100)        #procent av antal frön
        occupation_in_percent.append(Calculate:)
    print(percent)
    la = LandAnimation(land,plant,percent,rowdist)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50) # frames
    plt.show()

if __name__ == '__main__':
    from plantclass import TestLand as tl
    from plantclass import Test_Database as tps
    la = LandAnimation(tl,tps)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
    plt.show()
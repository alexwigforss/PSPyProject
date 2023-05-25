# Skriv ut grafer månad för månad som ritar ut placering (utgå från spridd sådd) av rätt antal fröer, och när de ska skördas

# Hitta frö med tidigast sådd, [rita ut rätt antal av fröet i grafen]

# [Hitta nästa frö-sådd, rita ut rätt antal]

# markera skördetid 

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# plt.ion()
class LandAnimation:
    #size = 100
    def __init__(self, land = '', plants=[]):
        self.land = land
        self.qoute = len(plants)
        print('qoute = ', self.qoute)
        self.size = 100
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(0, 0)
        self.plants = plants
        self.ListOfPlants = []
        L_INDEX = 0
        for each in plants:
            YSPACE = plants[L_INDEX].y
            XSPACE = plants[L_INDEX].x
            nr_of_hori=int(80/XSPACE) # rows
            nr_of_vert=int(120/YSPACE/self.qoute) # cols
            #print('nr_of_vert ',nr_of_vert)
            #print('YSpace: ' , YSPACE,'XSpace: ' , XSPACE)

            Y_START = 120/self.qoute*L_INDEX
            y = np.full((nr_of_hori, nr_of_vert), 0)
            for each in y:
                each[:] = np.arange(Y_START + YSPACE/2, Y_START + YSPACE*nr_of_vert+(YSPACE/2), YSPACE, dtype=float)

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
        self.title = plt.title("Namnet På Landet")
        # https://datavizpyr.com/how-to-draw-a-rectangle-on-a-plot-in-matplotlib/
        # https://www.statology.org/matplotlib-rectangle/
        self.ax.add_patch(plt.Rectangle((0, 0), self.land.height, self.land.width, fill = False),)

    def animate(self,i): # a.k.a update
        global size
        q = 0
        for each in self.ListOfPlants:
            if i < (self.plants[q].x)*10:
                # https://www.digitalocean.com/community/tutorials/numpy-ones-in-python
                each.set_sizes(np.ones(self.qoute)*i)
            q += 1
        tup = self.line,self.title
        # https://datagy.io/python-append-to-tuple/
        for each in self.ListOfPlants:
            tup = tup + (each,)
        return tup

def assembleLand(land, plants, percent_list):
    pass

if __name__ == '__main__':
    from plantclass import TestLand as tl
    from plantclass import TestPlants as tps
    la = LandAnimation(tl,tps)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
    plt.show()
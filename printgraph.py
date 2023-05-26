# Skriv ut grafer månad för månad som ritar ut placering (utgå från spridd sådd) av rätt antal fröer, och när de ska skördas

# Hitta frö med tidigast sådd, [rita ut rätt antal av fröet i grafen]

# [Hitta nästa frö-sådd, rita ut rätt antal]

# markera skördetid 

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
# from plantclass import TestLand as tl
import calculations as calc

# plt.ion()
class LandAnimation:
    def __init__(self, land = '', plants=[],percent=[],rowdist=True):

        self.land = land
        self.plants = plants
        self.percent=percent
        self.qoute = len(plants)
        self.qoutes = []
        self.ListOfPlants = []
        i = 0

        for each in range(len(plants)):
            q_ofplants = calc.num_to_range(percent[i],0,100,0.0,self.qoute)
            normalized = calc.num_to_range(q_ofplants,0,len(plants),0.0,1)
            self.qoutes.append(normalized)
            i+=1

        # print('qoute = ', self.qoute)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(0, 0)
        L_INDEX = 0
        Y_START = 2
        for each in plants:
            if rowdist:
                YSPACE = plants[L_INDEX].y
                XSPACE = plants[L_INDEX].x
            elif not rowdist:
                YSPACE = plants[L_INDEX].mid_dist
                XSPACE = plants[L_INDEX].mid_dist
                # width = x = hori,     height = y = vert

            nr_of_hori=int(land.width/XSPACE) # rows
            nr_of_vert=int(land.height/YSPACE*self.qoutes[L_INDEX]) # cols
            print(f"{each.name} antal vert: {nr_of_hori}, antal hori: {nr_of_vert}")
            #Y_START = land.height/self.qoute*L_INDEX #
            #Y_START = land.height/self.qoutes[L_INDEX]*2

            y = np.full((nr_of_hori, nr_of_vert), 0)
            #print(self.plants[L_INDEX].name,YSPACE,end=' ')
            #print(self.plants[L_INDEX].name,YSPACE,end=' ')
            
            # Placerar ut växter i raderna
            for each in y:
                each[:] = np.arange(Y_START + YSPACE/2, Y_START + (YSPACE*(nr_of_vert))+(YSPACE/2), YSPACE, dtype=float)
            Y_START = (percent[L_INDEX]/100*land.height) # - ev korrigering YSPACE/2
            #print("Ystart: ",Y_START)
            x = np.full((nr_of_hori, nr_of_vert), 0)
            
            # Placerar ut växter i kolumner
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

# Gör att plantorna växer
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
    
# Tar info från programkörningen
def assembleLand(land, complete_list, rowdist):
    plant= []
    percent=[]
    for each_plant in complete_list:
        plant.append(each_plant[0])
        percent.append(each_plant[1])        #procent av antal frön
    la = LandAnimation(land,plant,percent,rowdist)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50) # frames
    plt.show()

if __name__ == '__main__':
    from plantclass import TestLand as tl
    from plantclass import Test_Database as tps
    la = LandAnimation(tl,tps,50,False)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
    plt.show()
    #
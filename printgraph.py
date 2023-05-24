# Skriv ut grafer månad för månad som ritar ut placering (utgå från spridd sådd) av rätt antal fröer, och när de ska skördas

# Hitta frö med tidigast sådd, rita ut rätt antal av fröet i grafen 

# Hitta nästa frö-sådd, rita ut rätt antal

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
        #self.field = fields
        self.qoute = len(plants)
        print('qoute = ', self.qoute)
        self.size = 100
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = self.ax.plot(0, 0)
        # DOIN bygg ihop arrayer av fälten som skickas in

        YSPACE = plants[0].y
        XSPACE = plants[0].x
        nr_of_hori=int(80/XSPACE) # rows
        nr_of_vert=int(120/YSPACE/self.qoute) # cols
        print('nr_of_vert ',nr_of_vert)
        print(YSPACE)
        #y = np.array([[10,20,30,40,50],[10,20,30,40,50],[10,20,30,40,50]])
        y = np.full((nr_of_hori, nr_of_vert), 0)
        for each in y:
            each[:] = np.arange(YSPACE/2, YSPACE*nr_of_vert+(YSPACE/2), YSPACE, dtype=float)

        #x = np.array([[10,10,10,10,10],[20,20,20,20,20]])
        x = np.full((nr_of_hori, nr_of_vert), 0)
        i = 1
        for each in x:
            each[:]=XSPACE*i-XSPACE/2
            i+=1
        #x = np.full((5, 2), 1)
        s = np.full((nr_of_hori, nr_of_vert), 1000)

        self.dots = plt.scatter(y,x,s=s,label ="Allan")
        # https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
        # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
        self.legend = plt.legend(bbox_to_anchor =(0.25, 1.15), ncol = 2)
        # https://www.w3schools.com/python/matplotlib_labels.asp
        self.title = plt.title("Namnet På Landet")
        #https://datavizpyr.com/how-to-draw-a-rectangle-on-a-plot-in-matplotlib/
        #https://www.statology.org/matplotlib-rectangle/
        self.ax.add_patch(plt.Rectangle((0, 0), self.land.height, self.land.width,
                                        fill = False),)

        # TODO och plotta ut dem en i sänder
        # i=0
        # for e in y:
        #     self.dots = plt.scatter(e,x[i],s=100)
        #     i += 1

    def animate(self,i):
        global size
        # self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        self.dots.set_sizes(np.ones(self.x.size)*i)
        #self.dotsb.set_sizes(np.ones(self.x.size)*i)
        self.title.set_label('Baddaboom')
        #self.ax.set_title("|TW| = {}, Angle: {}°".format('a', 'b'))
        return self.line,self.dots,self.title
        #return self.line,self.dots,self.dotsb

if __name__ == '__main__':
    from plantclass import TestLand as tl
    from plantclass import TestPlants as tps
    la = LandAnimation(tl,tps)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
    plt.show()
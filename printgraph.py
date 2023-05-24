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
    def __init__(self, land = '', fields=[]):
        self.size = 100
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = self.ax.plot(0, 0)

        # TODO bygg ihop arrayer av fälten som skickas in
        y = np.array([[1,2,3,4,5],[1,2,3,4,5]])
        x = np.array([[1,1,1,1,1],[1.2,1.2,1.2,1.2,1.2]])
        s = np.full((2, 5), 1000)

        self.dots = plt.scatter(y,x,s=s,label ="Allan")
        # self.legend = plt.legend(['tomato','tomaato'])

        y = np.array([[1,1.5,2,2.5,3],[1,1.5,2,2.5,3]])
        x = np.array([[2,2,2,2,2],[2.2,2.2,2.2,2.2,2.2]])
        s = np.full((2, 5), 1000)

        self.dotsb = plt.scatter(y,x,s=s,label ="Ballan")
        # https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
        self.legend = plt.legend(bbox_to_anchor =(0.25, 1.15), ncol = 2)
        # https://www.w3schools.com/python/matplotlib_labels.asp
        self.title = plt.title("Namnet På Landet")
        self.ax.add_patch(plt.Rectangle((0, 0), tl.width, tl.height,
                                        fill = False),)
        # specify the location of (left,bottom),width,height

        # self.rect=plt.Rectangle((31,15),14,7, 
        #                 fill = False,
        #                 color = "purple",
        #                 linewidth = 2)

        # TODO och plotta ut dem en i sänder
        # i=0
        # for e in y:
        #     self.dots = plt.scatter(e,x[i],s=100)
        #     i += 1

    def animate(self,i):
        global size
        # self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        self.dots.set_sizes(np.ones(self.x.size)*i)
        self.dotsb.set_sizes(np.ones(self.x.size)*i)
        #self.legend.set_label(i)
        # print(i,end=' ')
        #return self.dots,self.dotsb
        return self.line,self.dots,self.dotsb

    # To save the animation, use e.g.
    #
    # ani.save("movie.mp4")
    #
    # or
    #
    # writer = animation.FFMpegWriter(
    #     fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save("movie.mp4", writer=writer)

if __name__ == '__main__':
    from plantclass import TestLand as tl
    la = LandAnimation(tl)
    ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
    plt.show()
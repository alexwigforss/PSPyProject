import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

plt.ion()
class LandAnimation:
    #size = 100
    def __init__(self):
        self.size = 100
        self.fig, ax = plt.subplots()

        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = ax.plot(self.x, np.sin(self.x))

        y = np.array([[1,2,3,4,5],[1,2,3,4,5]])
        x = np.array([[1,1,1,1,1],[1.2,1.2,1.2,1.2,1.2]])
        s = np.full((2, 5), 1000)

        self.dots = plt.scatter(y,x,s=s)

        # i=0
        # for e in y:
        #     self.dots = plt.scatter(e,x[i],s=100)
        #     i += 1

    def animate(self,i):
        global size
        self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        self.dots.set_sizes(np.ones(self.x.size)*i)
        # print(i,end=' ')
        return self.line,self.dots

    # To save the animation, use e.g.
    #
    # ani.save("movie.mp4")
    #
    # or
    #
    # writer = animation.FFMpegWriter(
    #     fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save("movie.mp4", writer=writer)

la = LandAnimation()
ani = FuncAnimation(la.fig, la.animate, interval=20, blit=True, save_count=50)
plt.show()
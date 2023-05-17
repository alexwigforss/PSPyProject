import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

y = np.array([1,2,3,4,5])
z = np.array([1,2,3,4,5])
dots = plt.scatter(y,z,s=200)
size = 200
#plt.ion()
def animate(i):
    global size
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    #size += 100
#    print('Animate ',end='')
    #dots.set_sizes([size] * 5)
    #dots.set_sizes(np.array([size,size,size,size,size]))
    dots.set_sizes(np.array([size+i,2,3,4,5]))
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
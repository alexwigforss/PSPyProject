# https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html#sphx-glr-gallery-shapes-and-collections-ellipse-collection-py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EllipseCollection

# .arange() => Return evenly spaced values within a given interval.
# .meshgrid()

x = np.arange(5)
y = np.arange(5)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 6.0
hh = Y / 6.0
aa = X * 1
sizes = np.array([[100,100],[80,80],[60,60],[40,40],[20,20]])
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=sizes,
                       offset_transform=ax.transData)
ec.set_array((X + Y).ravel())

ax.add_collection(ec)
ax.autoscale_view()
ax.set_xlabel('X')
ax.set_ylabel('y')
#cbar = plt.colorbar(ec)
#cbar.set_label('X+Y')
plt.show()
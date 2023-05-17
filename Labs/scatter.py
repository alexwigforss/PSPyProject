import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
z = np.array([3,3,3,3,3])

sizes = np.array([20,40,20,40,20])
# plt.ion()
plt.scatter(x,z,s=50)
#plt.scatter(x,y,s=sizes)
plt.show()
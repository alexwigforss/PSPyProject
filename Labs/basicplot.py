import matplotlib.pyplot as plt
import numpy as np
xplist = [1,1,2,3,4]
yplist = [1,2,2,3,4]

plt.plot(xplist, yplist, '*')
plt.show()

#Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
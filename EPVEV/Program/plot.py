# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([1, 2, 3, 4, 5], [10, 20, 25, 30, 100], color='lightblue', linewidth=3)
# ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
# ax.set_xlim(0.5, 4.5)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
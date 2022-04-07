import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

plt.plot(ypoints, ls = ':',marker='o')
plt.show()

# marker|line|color
plt.plot(ypoints, '*-.r')
plt.show()


plt.plot(ypoints, c = '#4CAF50')
plt.show()
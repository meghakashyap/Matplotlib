import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

xcoordinates = np.array([2,5,7,11,18]) 
plt.plot(xcoordinates,marker='o',ms=20, mec = '#4CAF50', mfc = '#4CAF50') 
plt.show() 
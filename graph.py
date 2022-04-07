import matplotlib.pyplot as plt 
import numpy as np 
xcoordinates=np.array([2,5,6,8])
ycoordinates = np.array([1,2,4,5]) 
plt.plot(xcoordinates,ycoordinates)
plt.show() 

# marking the graph
xcoordinates=np.array([0,6]) 
ycoordinates = np.array([0,6]) 
plt.plot(xcoordinates,ycoordinates,'*')
plt.show() 


# only with x axis
xcoordinates=np.array([1,2,6,8]) 
plt.plot(xcoordinates)
plt.show() 



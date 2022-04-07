import matplotlib.pyplot as plt
import numpy as np 
# plot 1: 
x = np.array([0, 1, 2, 3]) 
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1) 
plt.plot(x,y) 

# plot 2: 
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2) 
plt.plot(x,y) 
plt.show() 



#plot 1: 
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10]) 
fig,ax = plt.subplots(2, 2) 
plt.plot(x,y) 
plt.title("chart1") 
plt.xlabel("chart1xaxis") 
plt.ylabel("chart1yaxis") 
# here we are  giving space
ax[0,0].plot(x,x)
ax[0,1].plot(x,x*2) 
ax[1,0].plot(x,x*x) 
ax[1,1].plot(x,x*x*x) 

#plot 2: 
x = np.array([10, 16, 91, 45, 8]) 
y = np.array([21, 50, 71, 78, 13]) 
plt.subplot(1, 2, 2) 
plt.plot(x,y) 
plt.title("chart2") 
plt.xlabel("chart2xaxis") 
plt.ylabel("chart2yaxis") 
fig.tight_layout() 
plt.suptitle("my subplot") 
plt.show() 

#
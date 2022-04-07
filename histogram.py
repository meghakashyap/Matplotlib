import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

# Creating dataset
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]) 

# Creating histogram 
fig,ax = plt.subplots(figsize =(10, 7)) #(10,7) its a dimension /area 
ax.hist(a, bins = [0, 25, 50, 75, 100]) 
# Show plot 
plt.show() 
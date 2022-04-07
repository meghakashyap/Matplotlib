import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

# add labels
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

# shadow
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 


# color
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Grapes", "Dates"]
mycolors = ["red", "yellow", "g", "#F0B27A"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 



# To add a header to the legend, add the title parameter to the legend function.
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 
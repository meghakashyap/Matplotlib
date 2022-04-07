import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# vertical bar me width hoti hai
plt.bar(x,y,color="green",width=0.2)
plt.show()

# horizontal bar me height 
plt.barh(x,y,color = "red",height=0.2)
plt.show()


# other example
x = ["APPLES", "BANANAS"]
y = [400, 350]

plt.bar(x, y)
plt.show()
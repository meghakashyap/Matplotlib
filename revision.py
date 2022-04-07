import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

monthnumber=([1,2,3,4,5,6,7,8,9,10,11,12])
totalprofit=[100,600,700,800,760,750,76,74,98,87,65,43]
plt.subplot(4,3,1)
plt.plot(monthnumber,totalprofit)
plt.subplot(4,3,2)
plt.bar(monthnumber,totalprofit)
plt.subplot(4,3,3)
plt.barh(monthnumber,totalprofit)
plt.subplot(4,3,4)
plt.scatter(monthnumber,totalprofit)
plt.subplot(4,3,5)
plt.pie(monthnumber,labels=totalprofit)
plt.subplot(4,3,6)
plt.pie(monthnumber,totalprofit)
plt.show() 
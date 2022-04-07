# Read face cream and facewash product sales data and show it using the bar chart The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
# print(df)

x = np.array(df["month_number"])
z= np.array(df["facecream"])
y = np.array(df["facewash"])
ind = np.arange(len(z)) 

plt.xlabel("Month_Number")
plt.ylabel("Facewash and Facecream Sale")

plt.bar(x,z,color="b",width=0.2)
plt.bar(x,y,color="r",width=0.2)
plt.show()

# another way
plt.bar(ind,y,width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar(ind+0.25, z,width = 0.25,label = 'Face Wash sales data', align='edge')
plt.xticks(x) 
plt.grid(True, linewidth= 1, linestyle="--") 
plt.legend(loc='upper left')
plt.show()


# 2nd
df = pd.read_csv("company_sales_data.csv")
monthList = df ['month_number'].tolist()
faceCremSalesData = df ['facecream'].tolist() 
faceWashSalesData = df ['facewash'].tolist() 

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge') 

plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge') 

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

plt.legend(loc='upper left')
plt.title(' Sales data')
plt.xticks(monthList) 
plt.grid(True, linewidth= 1, linestyle="--") 
plt.title('Facewash and facecream sales data') 
plt.show() 



# Read toothpaste sales data of each month and show it using a scatter plot Also, add a grid in the plot. gridline style should “–“. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")

y = np.array(df["toothpaste"])
x = np.array(df["month_number"])

plt.xlabel("Month_Number")
plt.ylabel("Toothpaste Sale")

plt.scatter(x,y)
plt.grid(ls = '-')
plt.show()
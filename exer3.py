# Exercise 3: Read all product sales data and show it using a multiline plot Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ). 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
# print(df)

f = np.array(df["facecream"])
w = np.array(df["facewash"])
t = np.array(df["toothpaste"])
s = np.array(df["shampoo"])
m = np.array(df["moisturizer"])

plt.xlabel("Month_Number")
plt.ylabel("Sold Unit")

plt.plot(f,"o:")
plt.plot(w,"*-")
plt.plot(t,"d--")
plt.plot(s,"<")
plt.plot(m)
plt.show()
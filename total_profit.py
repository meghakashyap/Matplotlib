# Exercise 1: Read Total profit of all months and show it using a line plot Total profit data provided for each month. Generated line plot must include the following properties: – X label name = Month Number Y label name = Total profit 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
# print(df)

x = np.array(df["month_number"])
y = np.array(df["total_profit"])

plt.xlabel("Month_Number")
plt.ylabel("Toatl_Profit")

# using  line
plt.plot(x,y,"-o")
plt.show()

# using bar graph
plt.xlabel("Month_Number")
plt.ylabel("Toatl_Profit")
plt.bar(x, y)
plt.show()




# Get total profit of all months and show line plot with the following Style properties Generated line plot must include following Style properties: – Line Style dotted and Line-color should be red Show legend at the lower right location. X label name = Month Number Y label name = Sold units number Add a circle marker. Line marker color as read Line width should be 3 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
x = np.array(df["month_number"])
y = np.array(df["total_profit"])

plt.xlabel("Month_Number",)
plt.ylabel("Sold units")

# using  line
plt.plot(x,y,"o:r",linewidth = '3')
plt.show()
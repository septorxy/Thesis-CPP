import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [9.00, 6.500]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['generation', 'lowest_cost', 'highest_cost']

# Read a CSV file
df = pd.read_csv("Trackers/HighLow2.csv", usecols=columns[1::])
# gene = list(df["generation"])
# item1 = df["highest_cost"][0]
# item2 = list(df["lowest_cost"])[-1]
# y = [i for i in range(item1, item2, -10000)]
# Plot the lines
df.plot()


plt.show()
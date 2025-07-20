import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = "Bar chart/flight_delays.csv"
data = pd.read_csv(file_path, index_col="Month")

plt.figure(figsize=(14,7))
plt.title("Average arrival delay for each airline, by month")

sns.heatmap(data= data, annot= True)

plt.xlabel("Airline")
plt.show()
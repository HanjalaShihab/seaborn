import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = "Bar chart/flight_delays.csv"

data = pd.read_csv(file_path, index_col= "Month")

              #examine data:
print(data)

              #plotting bar chart:
plt.figure(figsize=(10, 6))
plt.title("Average arrival delay for spirit airlines flights, by month")

sns.barplot(x = data.index, y = data['NK'])

plt.ylabel("Arrival delay (in minutes)")
plt.show()
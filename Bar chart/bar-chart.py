import matplotlib.pyplot as plt
import pandas as pd

file_path = "Bar chart/flight_delays.csv"

data = pd.read_csv(file_path, index_col= "Month")

              #examine data:
print(data)

              #plotting bar chart:
plt.figure(figsize=(10, 6))
plt.title("Average arrival delay for spirit airlines flights, by month")

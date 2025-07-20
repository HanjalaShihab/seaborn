import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


                           #loading the data
file_path = "spotify/spotify.csv"

data = pd.read_csv(file_path, index_col="Date", parse_dates = True)


                           #examine the data
print(data.columns)
print("-------------------")
print(data.head())
print("-------------------")
print(data.tail())
print("-------------------")

                           #plotting the data
plt.figure(figsize=(16,6))

plt.title("Daily global streams of popular songs in 2017-2018")

sns.lineplot(data= data)
plt.show()
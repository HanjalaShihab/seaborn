import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "spotify/spotify.csv"
spotify = pd.read_csv(file_path, index_col= "Date", parse_dates= True)

plt.figure(figsize=(16,6))
plt.title("Daily global streams of popular songs in 2017-2018")

sns.lineplot(data=spotify['Shape of You'], label = "Shape of you")
sns.lineplot(data=spotify['Despacito'], label= "Despacito")

plt.xlabel("Date")
plt.show()
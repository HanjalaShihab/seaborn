import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


                           #loading the data
file_path = "lineplot/spotify.csv"
data = pd.read_csv(file_path, index_col="Date", parse_dates = True)


sns.set_style("dark")   ## Change the style of the figure to the "dark" theme

plt.figure(figsize=(12,6))

sns.lineplot(data= data)

plt.show()
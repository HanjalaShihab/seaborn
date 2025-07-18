import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "spotify/spotify.csv"

data = pd.read_csv(file_path, index_col="Date", parse_dates = True)

print(data.columns)
print("-------------------")
print(data.head())
print("-------------------")
print(data.tail())
print("-------------------")


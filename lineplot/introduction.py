import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fifa_filepath = "fifa.csv"

data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates= True)

print(data.info())
print("--------------------")
print(data.head())


plt.figure(figsize=(16,6))
sns.lineplot(data=data)
plt.show()
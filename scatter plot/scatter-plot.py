import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Usually, we use scatter plots to highlight the relationship between two continuous variables (like "bmi" and "charges"). 

file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)

x = insurance.head()
print(x)   #checking if the data is loaded properly

sns.scatterplot(x = insurance['bmi'], y = insurance['charges'])

plt.show()
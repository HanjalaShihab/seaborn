import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#We can use scatter plots to display the relationships between (not two, but...) three variables! 
# One way of doing this is by color-coding the points.

file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)

print(insurance.head())

sns.scatterplot(x = insurance['bmi'], y= insurance['charges'], hue=insurance['smoker'])

plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#To double-check the strength of scatterplot's relationship,
#  we can add a regression line, or the line that best fits the data. 
# We do this by changing the command to sns.regplot.

#If the regression line slopes upward, it suggests a positive relationship (as X increases, Y increases).
#If the line slopes downward, it's a negative relationship.

file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)

plt.figure(figsize=(10,6))
plt.title("Scatter plot for insurance")

sns.regplot(x = insurance['bmi'], y= insurance['charges'])

plt.show()
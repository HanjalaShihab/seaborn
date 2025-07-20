import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#This scatter plot shows that while nonsmokers to tend to pay slightly more with increasing BMI, smokers pay MUCH more.

#To further emphasize this fact, we can use the sns.lmplot command to add two regression lines, corresponding to smokers and nonsmokers.
#(You'll notice that the regression line for smokers has a much steeper slope, relative to the line for nonsmokers!)

file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)

plt.figure(figsize=(10,6))
plt.title("Nije nije try korlam!")

insurance.info()

print("-------------")


print(insurance.head())
sns.scatterplot(x = insurance["age"], y=insurance["bmi"], hue=insurance['smoker'])

plt.show()
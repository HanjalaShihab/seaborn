import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)

plt.figure(figsize=(10,6))
plt.title("Nije nije try korlam!")

insurance.info()

print("-------------")


print(insurance.head())
sns.scatterplot(x = insurance["age"], y=insurance["bmi"], hue=insurance['smoker'])

plt.show()
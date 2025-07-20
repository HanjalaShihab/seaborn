import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = "scatter plot/insurance.csv"
insurance = pd.read_csv(file_path)


sns.lmplot(x = "bmi", y= "charges", hue= "smoker", data= insurance)

plt.show()
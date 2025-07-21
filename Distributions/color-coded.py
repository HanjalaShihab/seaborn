import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = "Distributions/iris_renamed.csv"
iris = pd.read_csv(file_path, index_col="Id")


sns.displot(data= iris, x = iris['PL'], hue="Species")
#sns.kdeplot(data=iris, x='PL', hue='Species', shade=True)  #for kde/density plot

plt.show()
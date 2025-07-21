import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = "Distributions/iris_renamed.csv"
iris = pd.read_csv(file_path, index_col="Id")

print(iris.head())


sns.kdeplot(data= iris["PL"], shade = True)  #density plots
sns.jointplot(x = iris['PL'], y = iris['SW'] , kind="kde")  #2D KDE plots/density plots

plt.show()
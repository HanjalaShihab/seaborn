import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#loading the data:
file_path = "Distributions/iris.csv"
iris = pd.read_csv(file_path, index_col="Id")

#renaming the columns for better access:
iris = iris.rename(columns= {
    'Sepal Length (cm)': 'SL',
    'Sepal Width (cm)': 'SW',
    'Petal Length (cm)': 'PL',
    'Petal Width (cm)': 'PW'
})
print(iris.head())

#saving the coulmn names to a new csv file:
iris.to_csv("Distributions/iris_renamed.csv")

#plotting the histogram:
sns.histplot(iris['PL'])

plt.show()

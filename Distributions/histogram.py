import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = "Distributions/iris.csv"
iris = pd.read_csv(file_path, index_col="Id")

print(iris.head())
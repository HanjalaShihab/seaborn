import matplotlib.pyplot as plt
import pandas as pd

file_path = "Bar chart/fligh_delays.csv"

data = pd.read_csv(file_path, index_col= "Month")



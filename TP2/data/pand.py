import pandas as pd
df = pd.read_csv("dataset.csv", index_col="id")
""" print(df.describe()) """
print(df.head())
print(df.tail())
""" print(df) """

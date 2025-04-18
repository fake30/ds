import pandas as pd 

df = pd.read_csv("dataset2.csv")
data = pd.read_csv("dataset2.csv")
print(df)

df.dropna(inplace=True)
print("After Removing the rows with the empty cells")
print(df)

df2 = data.fillna(value=0)
print("After Filling the rows with the empty cells")
print(df2)


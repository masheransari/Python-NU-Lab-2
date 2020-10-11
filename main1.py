import pandas as pd


# a.	Read data1.csv and data2.csv as df1 and df2 dataFrames objects respectively. Use Pandas I/O libraries. Use column 0 as index for df1 and column 1 as index for df2. Print df1 and df2

index1 = [0, 1, 4]
index2 = [2,3]

df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")
df1.set_index("id",drop=True, inplace=True)
df2.set_index("id",drop=True, inplace=True)
print(df1)
print(df2)

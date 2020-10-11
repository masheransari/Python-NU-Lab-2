import pandas as pd
import numpy as np

# c.	Read data3.csv as df4 dataframe object and print df4 (not shown below). There are 2 new column ‘D’ and ‘E’ in this file. Merge df4 with df3 so that new dataframe (df5) has total 5 columns (A, B, C, D, E)

df1 = pd.DataFrame({
    'A': [1, 2, 4],
    'B': [2.0, 5.0, np.nan],
    'C': [3, 6, 5]
}, index=[0, 1, 4])

df2 = pd.DataFrame({
    'A': [2, 'Hello'],
    'B': [5, 3],
    'C': [6, 4]
}, index=[2, 3])

frames = [df1, df2]
df3 = pd.concat(frames)
print(df3.sort_index(inplace=True))

df4 = pd.DataFrame({
    'D': [np.nan, 1.0, np.nan, np.nan, 0.0],
    'E': [np.nan, 7.0, np.nan, np.nan, 8.0]
})

print(df4)
df5 = pd.merge(df3, df4,left_index=True,right_index=True)
print(df5)

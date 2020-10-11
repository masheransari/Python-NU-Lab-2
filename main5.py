import pandas as pd
import numpy as np

# e.	Replace Hello with NaN. Make it as general as possible so that all strings in dataframe df7 automatically becomes NaN

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
df3.sort_index(inplace=True)

df4 = pd.DataFrame({
    'D': [np.nan, 1.0, np.nan, np.nan, 0.0],
    'E': [np.nan, 7.0, np.nan, np.nan, 8.0]
})

# print(df4)
df5 = pd.merge(df3, df4, left_index=True, right_index=True)

# Now we assuming that we have a json file.

df6 = pd.read_json("assert/data.json")
# print(df6)

# newFrames = [df5, df6]

df7 = pd.concat([df5, df6], ignore_index=True)

listColumnsName = list(df7.columns.values)
df7.replace(to_replace="Hello",
            value=np.nan, inplace=True)
print(df7)


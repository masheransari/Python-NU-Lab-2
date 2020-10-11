import pandas as pd
import numpy as np

# b.	Modify (a) to concatenate df1 and df2 and assign it to df3. Print df3

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

frames = [df1,df2]
resultFrame = pd.concat(frames)
print(resultFrame)

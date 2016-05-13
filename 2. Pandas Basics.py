# 2nd tutorial
import pandas as pd
import numpy as np

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce_Rate': [65, 67, 78, 65, 45, 52]}
df = pd.DataFrame(web_stats)
# df2 = df.set_index('Day') # - bad method
# print(df2)

df.set_index('Day', inplace=True)  # good method
print(df)

print(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df.tail())

df3 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df3)
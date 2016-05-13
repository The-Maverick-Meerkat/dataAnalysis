import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)


df_std = df.describe()
print(df_std)
df_std = df.describe()['meters']['std']
print(df_std)

df = df[(df['STD'] < df_std)]  # the crux of the lesson - you can redefine a dataframe to adhere to certain operators
print(df)


df.plot()
plt.show()


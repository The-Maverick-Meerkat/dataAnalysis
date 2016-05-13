# 1st tutorial

import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt



start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 5, 7)

df = web.DataReader("XOM", "yahoo", start, end)

# print(df)
print(df.head())

df['High'].plot()
plt.legend()
plt.show()




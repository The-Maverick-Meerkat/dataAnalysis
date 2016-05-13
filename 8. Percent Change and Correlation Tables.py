import pandas as pd
import matplotlib.pyplot as plt
import quandl

# api_key = 'MtMS-NBs54bNdFK9ij-a'
#
#
#
# plt.style.use('fivethirtyeight')
#
# HPI_data = pd.read_pickle('pickle.pickle')
#
# # HPI_data['TX2'] = HPI_data['TX'] * 2
# # print(HPI_data[['TX','TX2']].head())
# # HPI_data = HPI_data.pct_change()




# def HPI_Benchmark():
#     df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
#     return df
#
#
# HPI_data['USA'] = HPI_Benchmark()
# # print(HPI_data.head())
#
# for i in range(len(HPI_data.columns)):
#     HPI_data.iloc[:,i] = 100.0 * (HPI_data.iloc[:,i] - HPI_data.iloc[0,i])/HPI_data.iloc[0,i]
#
# HPI_data.to_pickle('pickle2.pickle')

# print(HPI_data.head())
#


HPI_data = pd.read_pickle('pickle2.pickle')

HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)

# fig = plt.figure()
# ax1 = plt.subplot2grid((1, 1), (0, 0))
#
# HPI_data.plot(ax=ax1)
# HPI_data['USA'].plot(color='k',ax=ax1, linewidth=10)
#
#
# plt.legend().remove()
# plt.show()
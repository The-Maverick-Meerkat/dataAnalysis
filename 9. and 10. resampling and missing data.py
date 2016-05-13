
# resampling - choose one
HPI_data['TX1yr'] = HPI_data['TX'].resample('A')
HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how=mean) # mean(default), sum, ohlc (open high low close)




# missing data
print(HPI_data[['TX','TX1yr']])


# choose one
HPI_data.dropna(inplace=True)
HPI_data.dropna(how='all',inplace=True)
HPI_data.fillna(method='ffill',inplace=True)
HPI_data.fillna(method='bfill',inplace=True)
HPI_data.fillna(value=-99999,inplace=True)


HPI_data['TX'].plot(ax=ax1)
HPI_data['TX1yr'].plot(color='k',ax=ax1)
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
plt.legend().remove()
plt.show()
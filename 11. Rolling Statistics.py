

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
HPI_data = pd.read_pickle('pickle2.pickle')

# Rolling 12 entries Mean (in the data, every entry is a new month, so this is a trailing 12 months
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)

#Roling STD - needs a different graph
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)

HPI_data['TX'].plot(ax=ax1)
HPI_data['TX12MA'].plot(ax=ax1)
HPI_data['TX12STD'].plot(ax=ax2)

# Rolling correlation
TX_AK_12corr = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)

HPI_data['TX'].plot(ax=ax1, label="TX HPI")
HPI_data['AK'].plot(ax=ax1, label="AK HPI")
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2)


plt.show()
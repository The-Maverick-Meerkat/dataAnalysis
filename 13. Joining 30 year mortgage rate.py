import quandl

api_key = 'MtMS-NBs54bNdFK9ij-a'

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M', how='sum')
    print(df.head())
    return df

mortgage_30y()

# HPI_data = pd.read_pickle('fiddy_states3.pickle')
# m30 = mortgage_30y()
# HPI_Bench = HPI_Benchmark()
# m30.columns=['M30']
# HPI = HPI_Bench.join(m30)
# print(HPI.head())
#
# state_HPI_M30 = HPI_data.join(m30)
# print(state_HPI_M30.corr())
#
# print(state_HPI_M30.corr()['M30'])
#
#
# print(state_HPI_M30.corr()['M30'].describe())

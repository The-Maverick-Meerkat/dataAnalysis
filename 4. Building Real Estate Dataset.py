# import quandl
import pandas as pd

api_key = 'MtMS-NBs54bNdFK9ij-a'

# df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
# print(df.head())
f_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(f_states[0][0])

for abbv in f_states[0][0][1:]:
    print("FMAC/HPI_"+str(abbv))

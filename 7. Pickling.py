import quandl
import pandas as pd
import pickle


api_key = 'MtMS-NBs54bNdFK9ij-a'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial():
    states = state_list()
    main_df = pd.DataFrame()
    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [str(abbv)]
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    print(main_df.head())
    pickle_out = open('HPI_fifty_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close

# grab_initial()

pickle_in = open('HPI_fifty_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
# print(HPI_data.head())

HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2.head())
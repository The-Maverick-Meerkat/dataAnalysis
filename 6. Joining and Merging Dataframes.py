import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'year':[2001, 2002, 2003, 2004]})

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'year':[2005, 2006, 2007, 2008]})

df3 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53],
                    'year': [2001, 2002, 2003, 2004]})

# print(pd.merge(df1,df2, on='HPI')) # not good!!
# print(pd.merge(df1,df2, on=['HPI','Int_rate'])) # still not good!!

# df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)
# joined = df1.join(df3)
# print(joined)

merged = pd.merge(df1, df3, on=['year', 'HPI'])
merged = merged.astype('int64')
# merged.set_index('year', inplace=True)
# print(merged)

merged2 = pd.merge(df1, df2, on=['year','HPI', 'Int_rate','US_GDP_Thousands'], how='outer')
merged2 = merged2.astype('int64')
# merged2.set_index('year', inplace=True)
# print(merged2)

merged3 = pd.merge(merged, merged2, how='outer')
merged3.fillna(value=-99999, inplace=True)
merged3 = merged3.astype('int64')
merged3.set_index('year', inplace=True)
print(merged3)
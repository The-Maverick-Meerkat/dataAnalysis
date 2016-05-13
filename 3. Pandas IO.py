import pandas as pd

df = pd.read_csv('ZILL-Z77006_MLP.csv', index_col=0)
df.columns = ['Austin_HPI']
print(df.head())
df.to_csv('newcsv.csv')
df.to_csv('newcsv2.csv', header=False)
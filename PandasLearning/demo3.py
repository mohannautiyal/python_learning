import pandas as pd

df1 = pd.read_json('samplejson.txt')
# df1.info()
df1.index = ['A','B','C']
# print(df1.iloc[1])  #passing the index of the row
# print(df1.index.tolist() )
# print(df1.loc['B'])


# selecting single columns
print(df1.loc['B','name'])
print(df1.iloc[1,1])



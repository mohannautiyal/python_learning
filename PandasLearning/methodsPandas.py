import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

df1 = pd.read_json('samplejson.txt')
df2 =  pd.read_json('samplejson1.txt')

pd.set_option("display.max_rows",30 )
pd.set_option("display.max_columns",100 )
pd.set_option('display.width', 1000)

# print(df1.compare(df2,result_names=('Pre','Post')))
# seriesdata = df1.iloc(0)

# for i, seriesdatum in enumerate(seriesdata):

print(df1)
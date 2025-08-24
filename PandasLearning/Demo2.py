import pandas as pd

pd.set_option("display.max_rows",30 )
pd.set_option("display.max_columns",100 )
pd.set_option('display.width', 1000)

# Pandas use the loc attribute to return one or more specified row(s)

df1 = pd.read_json("samplejson.txt")
# print(df1.index)
# print(df1.loc[1])
# print(df1.loc[[1,0]])

# print(df1.to_string())

# Print the first 5 rows of the DataFrame:
# print(df1.head())
# print(df1.info())

# print(df1.columns)
# print(type(df1))
# print(df1)
# print(f"{df1['id']}  name is {df1['name']}")

for index,row in df1.iterrows():
    print("************************************")
    for col in df1.columns:
        print(f" {col}  {df1[col]}")
    # for col in row[index]:
    #    print(col)


    

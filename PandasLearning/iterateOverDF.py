import pandas as pd

df = pd.read_json('samplejson.txt')
# print(df)

# iterate over rows using iterrows() and itertuples

# for row in df.iterrows():
for row in df.itertuples():
    print("_______________________________________________")
    print(row)




import pandas as pd

df = pd.read_json("samplejson.txt")

# iterate over columns using items() method

for colname,colval in df.items():
    print("--------------------------------")
    print(f"Column Name is   {colname} :")
    print(colval)


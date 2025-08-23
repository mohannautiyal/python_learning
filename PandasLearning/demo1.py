import pandas as pd

# Empty dataframe
# df1 = pd.DataFrame()
# print(df1)

# Dataframe from list
# lstStudents = ["Ram","Shyam","Raj","Sohan"]
# df = pd.DataFrame(lstStudents)
# print(df)

# Dataframe from dict
lstSudents =["Raj","Shyam","Sohan","Mohan"]
lstDegree=["Bsc","Bcom","Btech","BA"]
lstScore=[100,200,400,200]
dict ={'empName':lstSudents ,'degree':lstDegree,'score':lstScore}

df_students =pd.DataFrame(dict)
print(df_students)

print(df_students.index)
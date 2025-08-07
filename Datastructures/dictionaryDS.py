# Dictionary data structure
# Represent individual objects as a key value pairs --> Dictionary
# Duplicate keys are not allowed but duplicate values are allowed
# Heterogeneous Objects
# insertion order is preserved
# Dynamic and mutable
# indexing and slicing are not applicable
# key --> gateway

# creation of dictionary
# d={}
# d = dict()
# print(type(d))

st=dict()
st["name"] = "Madan"
st["Age"]=24
st["Branch"] = "IT"

ol = [st]
st1=dict()
st1["name"] = "Rohan"

st1["Age"]=25
st1["Branch"] = "CS"

ol.append(st1)
ls =[st1,st]
print(ls)
print(ol)

emp ={"name":"Raj","Dept":"IT","Designation":"Test Lead"}
print(emp)

# Access Data
emp["rating"] =1
print(emp.get("name"))
print(emp["name"])
print(emp)

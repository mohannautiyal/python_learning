# Tuple is same as list. It is immutable
# Read only version of list. Not dynamic
# () separated by comma

Emp = ("Madan","Rohan")
print(Emp)

c = Emp.count("Madan")
print(c)

print(len(Emp))

for st in Emp:
    print(st + " Good Morning")

print(Emp[0] + "  "+ Emp[1])

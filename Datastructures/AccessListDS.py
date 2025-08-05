mynumlist = list(range(10,50,5))


# Using slice operator
print(mynumlist[0:4])

mynumlist[0]=1000
print(mynumlist)

# Traversing
for n in mynumlist:
    print(n)

# functions
print(len(mynumlist))
mynumlist.append(3000)
print(mynumlist)
mynumlist.reverse()
print(mynumlist)
mynumlist.sort()
print(mynumlist)

mynumlist.append(1000)
print(mynumlist.count(1000))

mynewlist =list((range(50,60)))
mynumlist.extend(mynewlist)
print(mynumlist)

mynumlist.remove(1000) # This will remove first occurence of 1000
print(mynumlist)

# Nested List
EmpDet01 = ["Madan","Test Manager","Fidelity"]
EmpDet02 = ["Sohan","Test Lead","Fidelity"]
EmpDet03 = ["Rohan","Test Analyst","Fidelity"]

CompanyEmp =[EmpDet01,EmpDet02,EmpDet03]
print(CompanyEmp[2][1])
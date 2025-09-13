
stud = dict()
stud["name"]= "Mohan"
stud["class"]= "V"
stud["subject"]="Maths"

# print(stud)
empdetails =[]
empdetails.append(stud)
stud = dict()

stud["name"]= "Rohan"
stud["class"]= "VI"
stud["subject"]="English"
empdetails.append(stud)

studName = "Mohan"
print(empdetails)
for st in empdetails:
    if studName == st["name"]:
        # print(stud["subject"])
        print("Matched")
    else:
        print(studName,stud["name"])





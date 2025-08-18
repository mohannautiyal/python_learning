class employee:

    def __init__(self,name,surname):
        self.name =name
        self.surname = surname

    def displayname(self,strName=None,strSurname=None):
        if strName is not None and strSurname is not None:
            return f"{strName} {strSurname}"
        elif strSurname is None:
            return strName
        else:
            return strSurname


emp = employee("Madan","Nautiyal")

print(emp.displayname("Name","Surname"))

print(emp.displayname("Name"))


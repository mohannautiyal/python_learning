# Features of OOPS
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

class employee:
    # name=""
    # department=""
    # designation=""
    def __init__(self,name,department,designation):
        self.name =name
        self.department =department
        self.designation = designation

    def show_emp_details(self):
        print(self.name, " ", self.designation)
        print(f"{self.name} is in {self.department}")


emp1 = employee("Madan","IT","Test Analyst")
emp2 = employee("Aman","Support","Test Manager")
emp1.show_emp_details()

print(emp1.__dict__)

# del(emp2)
print(emp2.name)
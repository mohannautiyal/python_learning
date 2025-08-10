# Abstraction Hiding unnecessary details from users through class and methods

# Encapsulation Restrict access to certain attributes or methods to protect data and enforce
# controlled access

class student:

    def __init__(self,name,standard,percentage):
        self.name = name
        self.standard = standard
        self.__percentage=percentage


    def showStudentDetails(self):
        print(self.name)
        print(self.standard)
        print(self.__percentage)


student1 = student("Madan","V",97)

student1.showStudentDetails()
print(student1.name)
# print(student1.percentage)


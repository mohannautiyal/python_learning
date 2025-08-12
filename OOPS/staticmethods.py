class car:

    def __init__(self,model,company):
        self.model = model
        self.company = company

    def showcar(self):
        print(self.model,"  ",self.company)

    @staticmethod
    def runcar():
        print("Car is running ")


c =car("Altroz ","TATA")
c.showcar()

car.runcar() #calling static method


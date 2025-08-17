
class bankAccount:

    def __init__(self,name,account_number):
        self._name = name
        self._account_number = account_number
        # self._email =self._name + "@gmail.com"


    def showaccountdetails(self):
        print("+++++++++++++++++++++++++++++++++")
        print("Account Holder ",self._name)
        print("Account Number is ",self._account_number)
        # print(self._email)

    def email(self):
        return  f"{self._name}@gmail.com"

acc = bankAccount('Rishita','1234678')

acc.showaccountdetails()
print(acc.email())
# acc.showemail()


acc._name = "Kavya"
acc.showaccountdetails()
# acc.showemail()
print(acc.email())

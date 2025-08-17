
class bank_Account:

    def __init__(self,name,account_number):
        self._name = name
        self._account_number = account_number


    def showaccountdetails(self):
        print("+++++++++++++++++++++++++++++++++")
        print("Account Holder ",self._name)
        print("Account Number is ",self._account_number)
        # print(self._email)

    @property
    def email(self):
        return  f"{self._name}@gmail.com"

    
acc = bank_Account('Rishita','1234678')

acc.showaccountdetails()
print(acc.email)


acc._name = "Kavya"
acc.showaccountdetails()
print(acc.email)

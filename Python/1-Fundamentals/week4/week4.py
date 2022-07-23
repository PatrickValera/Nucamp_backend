# OOP
from unicodedata import name


class User:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def change_password(self,password):
        self.password=password
    
class BankUser(User):
    def __init__(self,name,password):
        super().__init__
        self.balance=0
    def checkBalance(self):
        print(f'Balance: {self.balance}')

bank_user1=BankUser("pat","password")
bank_user1.checkBalance()
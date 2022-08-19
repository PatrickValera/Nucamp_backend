class User:
    def __init__(self,name,pin,password) -> None:
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self,value):
        self.name=value
    def change_pin(self,value): 
        self.pin=value
    def change_password(self,value):
        self.password=value


class BankUser(User):
    def __init__(self, name, pin, password) -> None:
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has a balance of {self.balance}")

    def withdraw(self,value):
        self.balance-=value
        self.show_balance()
        
    def deposit(self,value):
        self.balance+=value
        self.show_balance()

    def transfer_money(self,value,recepient:"BankUser"):
        print(f"You are transferring ${value} to {recepient.name}")
        print("Authentication Required")
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print("Transfer Authorized")
            self.balance-=value
            self.show_balance()
            recepient.balance+=value
            recepient.show_balance()
            return True
        else: return False

    def request_money(self,value,sender:"BankUser"):
        print(f"You are requesting ${value} from {sender.name}")
        print("User authentication is required")
        entered_pin = input("Enter {sender.name}'s PIN: ")
        if entered_pin == sender.pin:
            entered_password = input ("Enter your password: ")
            if entered_password == self.password:
                self.balance+=value
                sender.balance-=value
                self.show_balance()
                sender.show_balance()
                return True
            else:
                print("Invalid Password. Transaction canceled.")
        else:
            print("Invalid Pin. Transaction canceled")
            return False





""""Driver Code for Task 1"""
'''user1=User("BOB","1234","password")
print(user1.name,user1.pin,user1.password)'''


""""Driver Code for Task 2"""
'''user1=User("BOB","1234","password")
user1.change_name("Bobby")
user1.change_pin("4321")
user1.change_password("newpassword")
print(user1.name,user1.pin,user1.password)'''


""" Driver Code for Task 3"""
'''user1=BankUser("BOB","1234","password")
print(user1.name,user1.pin,user1.password,user1.balance)'''

""" Driver Code for Task 4"""
'''user1=BankUser("BOB","1234","password")
user1.show_balance()
user1.deposit(1000)
user1.withdraw(500)'''

""" Driver Code for Task 5"""
'''user1=BankUser("BOB","1234","password")
user2=BankUser("Alice","0000","password")
user1.deposit(1000)
user1.transfer_money(500,user2)'''


from unicodedata import name
from bankaccount import BankAccount
# from unicodedata import name

# from bankaccount import BankAccount

class User:
    def __init__(self,name,email):
        self.name= name 
        self.email= email
        self.account = BankAccount(int_rate=.02, balance=0)
    
    def make_deposit(self): 
        self.account.deposit(1000)
        print(self.account.balance)
        return self
    
    def make_withdrawal(self):
        self.account.withdraw(-100)
        print(self.account.balance)
        return self
    
    def display_user_balance(self):
        print (f'User:{self.name}, Savings Balance:{self.account.balance}')

John=User("John", "john@ninja.com")
jill=User ("Jill", "jill@ninja.com")

John.display_user_balance()
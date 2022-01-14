class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -=amount
        return self

    def display_user_balance(self):
        print (f'user: {self.name} balance: {self.account_balance} ')



john=User("John Ninja", "john@ninja.com")
jane=User("Jane Python", "jane@python.com")
jill=User("Jill Java", "jill@java.com")


john.make_deposit(100).make_deposit(300).make_deposit(200).make_withdrawl(300).display_user_balance()

jane.make_deposit(400).make_deposit(600).make_withdrawl(500).make_withdrawl(500).display_user_balance()

jill.make_deposit(1000).make_withdrawl(200).make_withdrawl(200).make_withdrawl(200).display_user_balance()


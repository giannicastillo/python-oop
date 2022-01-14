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

john.make_deposit(100)
john.make_deposit(200)
john.make_deposit(300)
john.make_withdrawl(300)
john.display_user_balance()

jane.make_deposit(400)
jane.make_deposit(600)
jane.make_withdrawl(500)
jane.make_withdrawl(500)
jane.display_user_balance()

jill.make_deposit(1000)
jill.make_withdrawl(200)
jill.make_withdrawl(200)
jill.make_withdrawl(200)




class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate =int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance<amount):
            print (f'Insufficient funds: Charging a $5 fee')
            self.balance-= (5+amount)
            return self
        self.balance -= amount
        return self

        
    def display_account_info(self):
        print (f' balance: ${self.balance} ')
        return self

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        print (f'{self.balance}')
        return self


savings  = BankAccount(.1 , 0)
checking= BankAccount (.1 , 0)

savings.deposit(500).deposit(500).deposit(500).withdraw(500).display_account_info()
checking.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

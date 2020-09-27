class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account name: {self.owner} how much money: {self.balance}"

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self.balance


    def withdraw(self, amount):

        if (self.balance - amount >= 1):
            self.balance = self.balance - amount
            print(self.balance)
            return self.balance

        else:
            print('Not enough money in balance')





# 1. Instantiate the class
acct1 = Account('Jose',100)

acct2 = Account('Jonas',1000)

# # # 2. Print the object
# print(acct1)
# print(acct2)

# 3. Show the account owner attribute
acct1.owner

# # # 4. Show the account balance attribute
acct1.balance

# # 5. Make a series of deposits and withdrawals
# acct1.deposit(50)

acct1.withdraw(10)

# # 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500)
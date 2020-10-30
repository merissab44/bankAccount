class BankAccount:
    balance = 0
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.__account = account_number
        self.__routing = routing_number
        self.balance = balance

    def deposit(self, amount):
        amount = amount
        self.balance += amount + self.balance
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        amount = amount
        self.balance = self.balance - amount
        print(f"Amount Withdrawn: ${amount}")
    def get_balance(self):
        print(f"Your current balance: ${self.balance}")
        return self.balance
class BankAccount:
    balance = 0
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.__account = account_number
        self.__routing = routing_number
        self.balance = balance
        s = account_number[-4:].rjust(len(account_number), '*')
        print(s)

    def deposit(self, amount):
        self.balance += amount + self.balance
        print(f"Amount Deposited: ${amount}")
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Amount Withdrawn: ${amount}")
        return self.balance

    def get_balance(self):
        balance = self.balance
        print(f"Your current balance: ${self.balance}")
        return balance

    def print_receipt(self):
        print(self.name)
        print(f"Account No.:  {str.replace(str(self._BankAccount__account[:-4]), "X")}" + f"{str(self._BankAccount__account)[-4:]}")
        print(f"Routing No.: {self._BankAccount__routing}")
        print(f"Balance: ${self.balance}")

merissa = BankAccount('Merissa Bridgeman', '193039494', '43940303939', 0)
"""menu option at beginning so user can choose which poem to see"""
while True:
    choice = input(""" Please enter from the options below:
                1: deposit
                2: withdraw
                3: get balace 
                4: print a receipt """)
    if choice == "1":
        amount = int(input("how much would you like to deposit? "))
        print(merissa.deposit(amount))
    elif choice == "2":
        amount = int(input("how much would you like to withdraw? "))
        print(merissa.withdraw(amount))
    elif choice == "3":
        print(merissa.get_balance())
    elif choice == "4":
        print(merissa.print_receipt())

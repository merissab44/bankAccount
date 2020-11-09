import re
class BankAccount:
    # set the initial balance of the account to 0
    balance = 0
    # these are attributes that every bank account share in common
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.__account = account_number
        self.__routing = routing_number
        self.balance = balance
# these are the start of the methods, first one depsits money to your account balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        return self.balance
# this method subtracts money from account balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Amount Withdrawn: ${amount}")
        return self.balance
# this method shows current account balance
    def get_balance(self):
        balance = self.balance
        return balance
    def add_interest(self):
        interest = self.balance * 0.00083
        balance = self.balance - interest
        print (f"You were charged {interest} in interest. Your remaining balance is: {balance}")
        return balance
# this method gives an overview of your account
    def print_receipt(self):
        balance = self.balance
        print(self.name)
        # from w3schools this looks for digits in this string and replaces the first 4 with an asterisk
        account = re.sub("\d","*",str(self._BankAccount__account), 4)
        print(f"Account No.: {account}")
        print(f"Routing No.: {self._BankAccount__routing}")
        print(f"Balance: ${balance}")
# initiated 3 new bank account objects
merissa = BankAccount('Merissa Bridgeman', 19339494, 43940303939, 600)
audrey = BankAccount('Audrey Byrne', 38492049, 498493947,400)
wendy = BankAccount('Wendy Chambers', 48393028, 374803483, 1800)
"""menu option at beginning to give user atm feel"""
    #takes input of person
person = input("Please enter first name: ")
#this will loop so for each person, it'll go back to the menu if another action is taken
while True:
    #This takes the input of a name and links it to the bank account
    if person == "merissa":
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
            print(merissa.add_interest())
        elif choice == "4":
            print(merissa.print_receipt())
    elif person == "audrey":
        choice = input(""" Please enter from the options below:
                        1: deposit
                        2: withdraw
                        3: get balace 
                        4: print a receipt """)
        if choice == "1":
            amount = int(input("how much would you like to deposit? "))
            print(audrey.deposit(amount))
        elif choice == "2":
            amount = int(input("how much would you like to withdraw? "))
            print(audrey.withdraw(amount))
        elif choice == "3":
            print(audrey.add_interest())
        elif choice == "4":
            print(audrey.print_receipt())
    elif person == "wendy":
        choice = input(""" Please enter from the options below:
                        1: deposit
                        2: withdraw
                        3: get balace 
                        4: print a receipt """)
        if choice == "1":
            amount = int(input("how much would you like to deposit? "))
            print(wendy.deposit(amount))
        elif choice == "2":
            amount = int(input("how much would you like to withdraw? "))
            print(wendy.withdraw(amount))
        elif choice == "3":
            print(wendy.add_interest())
        elif choice == "4":
            print(wendy.print_receipt())

class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.__account = account_number
        self.__routing = routing_number
        self.balance = balance

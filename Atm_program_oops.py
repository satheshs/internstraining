class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.ac_number = account_number
        self.balance = balance
        print("Account Number:", self.ac_number)

    def account_details(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.ac_number}")
        print(f"Balance: {self.balance}")

class Deposit:
    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Amount deposited:", amount)

class Withdraw:
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance!!!!")

class Transaction_history(BankAccount, Deposit, Withdraw):
    def __init__(self, name, account_number, balance=0):
        BankAccount.__init__(self, name, account_number, balance)
        self.account_details()

    def transaction_history(self):
        print(f"Transaction History for the Account Number: {self.ac_number}")
        print(f"Current_balance: {self.balance}")

name = input("Enter the Account Holder Name: ")
ac_no = int(input("Enter the Account Number: "))

my_obj = Transaction_history(name, ac_no)
my_obj.deposit()
my_obj.withdraw()
my_obj.transaction_history()

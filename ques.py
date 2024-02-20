# Consider the Python program that simulates an ATM system using Object-Oriented Programming concepts, including Account, Transaction, Deposit, and Withdrawal classes. The program allows users to create accounts, perform transactions, display balances, and view transaction histories. (Can use Python CLI to get the input from the user).
# Write a program that incorporates Object-Oriented Programming principles such as inheritance, encapsulation, and polymorphism. Provide specific examples from the code to illustrate these concepts.

# encapsulation--In encapsulation I had create the parent class(Account) in that i had provided the methods
import logging

logging.basicConfig(level=logging.DEBUG, filename='atm_Account.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Account:
    def __init__(self,name,accNo,balance=0):
        self.name=name
        self.accNo=accNo
        self.balance=balance
        self.transactions = []

    def acc_creation(self):
        print(f"account holder name:{self.name}")
        print(f"account number:{self.accNo}")
        print(f"balance:{self.balance}")

    def available_balance(self):
        print(f"Available balance:{self.balance}")

    def transaction_history(self):
        return [str(transaction) for transaction in self.transactions]



class Deposit:
    def deposit(self):
        amount=float(input("Enter an amount to deposit:"))
        self.balance +=amount
        print("deposited amount:",self.balance)

class Withdraw:
    def withdraw(self):
       
        # self.balance>=amount
        print("After withdrew amount the balance is:", self.balance)

# inheritence--In inheritence I passed parent classes(Account,Deposit,Withdraw) to the child class(Transaction)
class Transaction(Account,Deposit,Withdraw):

    # polymorphism--In polymorphism i have used the same method deposit and withdraw in both Parent classes(Deposit and Withdraw) as well as the child class(Transaction)
    def deposit(self):
        super().deposit()
        self.transactions.append(f"{self.balance}-Deposited amount")

    def withdraw(self):

      try:
            amount = float(input("Enter an amount to withdraw:"))
            if amount > self.balance:
                logging.warning("Enter the amount within the balance")
                raise ValueError("Insufficient funds.")

            self.balance -= amount
            super().withdraw()
            self.transactions.append(f"{self.balance}-The balance after Withdrew amount")
            logging.info(f'Withdrawal of {amount} made from account {self.accNo}')
      except ValueError as e:
          print(f"Error: {e}")

name=input("Enter the account holder name:")
accNo=int(input("Enter the account number:"))

obj=Transaction(name,accNo)
obj.acc_creation()
obj.deposit()
obj.withdraw()
obj.available_balance()
transactions = obj.transaction_history()

print("\nTransaction History:")
for transaction in transactions:
             print(transaction)


# output
# Enter the account holder name:Rajeswari R
# Enter the account number:678913412771
# account holder name:Rajeswari R
# account number:678913412771
# balance:0
# Enter an amount to deposit:10000
# deposited amount: 10000.0
# Enter an amount to withdraw:2000
# After withdrew amount the balance is: 8000.0
# Available balance:8000.0
#
# Transaction History:
# 10000.0-Deposited amount
# 8000.0-The balance after Withdrew amount

# Enter the account holder name:Rajeswari R
# Enter the account number:67893420398
# account holder name:Rajeswari R
# account number:67893420398
# balance:0
# Enter an amount to deposit:1000
# deposited amount: 1000.0
# Enter an amount to withdraw:1100
# Error: Insufficient funds.
# Available balance:1000.0
#
# Transaction History:
# 1000.0-Deposited amount














class Account:
    def __init__(self, name, accno):
        self.name = name
        self.accno = accno
        self.bal = 0
        self.history = []

    def deposit(self, amount):
        
        if amount > 0:
            self.bal += amount
            self.history.append(f"Deposited - {amount}")
            return "Successfully deposited!"
        else:
            return "Amount should be greater than 0"

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.history.append(f'Withdraw - {amount}')
            return "Successfully withdrawn!"
        else:
            return "Insufficient balance!"

    def check_balance(self):
        return self.bal

    def check_history(self):
        if not self.history:
            return "Empty history!"
        return self.history




print("Enter the Name :")
name=input()
print("Enter acc No: ")
accno=int(input())

a1 = Account(name, accno)
print("Enter the number you want:")
while True:
    print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Check history\n5. Exit")
    ch = int(input())
    if ch == 1:
        print()
        print("Balance:", a1.check_balance())
        print()
            
    elif ch == 2:
        amount = int(input("Enter the amount to deposit: "))
        print()
        print(a1.deposit(amount))
        print()
    elif ch == 3:
        amount = int(input("Enter the amount to withdraw: "))
        print()

        print(a1.withdraw(amount))
        print()
    elif ch == 4:
        print("Transaction history:", a1.check_history())

        print()
    elif ch == 5:
        break
    else:
        print("Choose a correct option.")


class Account:
    def __init__(self, name, pin, balance=0):
        self._name = name
        self._pin = pin
        self._balance = balance
        self._transactions = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        self._pin = new_pin

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, new_transactions):
        self._transactions = new_transactions

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self._balance += amount
            self._transactions.append(f"Deposit: +{amount}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self, amount, final_amount=None):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if final_amount is None:
                final_amount = amount
            if self._balance >= final_amount:
                self._balance -= final_amount
                self._transactions.append(f"Withdrawal: {amount} with Service Charge Totally => -{final_amount}")
            else:
                print("Insufficient funds")
        except ValueError as e:
            print(f"Error: {e}")

    def display_balance(self):
        print(f"Account Balance for {self.name}: ${self.balance}")

    def display_transactions(self):
        print(f"Transaction History for {self.name}:")
        for transaction in self.transactions:
            print(transaction)

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, pin):
        if name in self.accounts:   
            print("Account already exists")
        else:
            self.accounts[name] = Account(name, pin)
            print("Account created successfully")

    def select_account(self, name, pin):
        if name in self.accounts and self.accounts[name].pin == pin:
            return self.accounts[name]
        else:
            print("Account not found or incorrect PIN")
            return None

    def start(self):
        while True:
            print("\n1. Create Account")
            print("2. Select Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Display Balance")
            print("6. Display Transactions")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                self.create_account(name, pin)
            elif choice == '2':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.select_account(name, pin)
                if account:
                    self.manage_account(account)
            elif choice == '3':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.select_account(name, pin)
                if account:
                    amount = input("Enter deposit amount: ")
                    account.deposit(amount)
            elif choice == '4':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.select_account(name, pin)
                if account:
                    amount = input("Enter withdrawal amount: ")
                    print("1. Current Account\n2. Savings Account")
                    account_type = input("Enter Account Type (1 or 2): ")
                    if account_type == '1':
                        final_amount = float(amount) * 1.5
                        account.withdraw(amount, final_amount)
                    elif account_type == '2':
                        account.withdraw(amount)
                    else:
                        print("Please provide proper account details")
            elif choice == '5':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.select_account(name, pin)
                if account:
                    account.display_balance()
            elif choice == '6':
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.select_account(name, pin)
                if account:
                    account.display_transactions()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def manage_account(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Display Transactions")
            print("5. Back to Main Menu")

            choice = input("Enter choice: ")

            if choice == '1':
                amount = input("Enter deposit amount: ")
                account.deposit(amount)
            elif choice == '2':
                amount = input("Enter withdrawal amount: ")
                print("1. Current Account\n2. Savings Account")
                account_type = input("Enter Account Type (1 or 2): ")
                if account_type == '1':
                    final_amount = float(amount) * 1.5
                    account.withdraw(amount, final_amount)
                elif account_type == '2':
                    account.withdraw(amount)
                else:
                    print("Please provide proper account details")
            elif choice == '3':
                account.display_balance()
            elif choice == '4':
                account.display_transactions()
            elif choice == '5':
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    atm = ATM()
    atm.start()

from datetime import datetime

class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now()
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type} ${self.amount}"

class PersonalFinanceManager:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def record_transaction(self, transaction):
        if transaction.transaction_type == "deposit":
            success = self.accounts[transaction.account].deposit(transaction.amount)
        elif transaction.transaction_type == "withdrawal":
            success = self.accounts[transaction.account].withdraw(transaction.amount)
        else:
            success = False
        
        if success:
            self.transactions.append(transaction)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts.values())


# personal finance manager
pfm = PersonalFinanceManager()

# add accounts
# account number 12345 with an initial balance of $1000
pfm.add_account(Account("12345", 1000))  
# account number 67890 with an initial balance of $500
pfm.add_account(Account("67890", 500))   

# record transactions
# deposit $200 into account 12345
pfm.record_transaction(Transaction("12345", 200, "deposit"))    
# withdraw $150 from account 67890
pfm.record_transaction(Transaction("67890", 150, "withdrawal")) 
# withdraw $100 from account 12345
pfm.record_transaction(Transaction("12345", 100, "withdrawal")) 

# transactions
for transaction in pfm.transactions:
    print(transaction)

# total balance across all accounts
print(f"Total Balance: ${pfm.get_total_balance()}")


from tabulate import tabulate
from datetime import datetime
from zoneinfo import ZoneInfo

ARIZONA_TZ = ZoneInfo("America/Phoenix")  # Arizona (no DST)


def now_arizona():
    """Current date/time in Arizona, formatted for display."""
    return datetime.now(ARIZONA_TZ)


"""
Bank Simulator: 
1. Create an Account 
2. Add money 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Check Balance
8. Exit 
Structure of Account: 
Account Number: 
Holder Name: 
Account Type: 
Age: 
Balance: 
PIN: 
Structure of Transaction:
Transaction ID: 
Type: 
From Account: 
To Account: 
Amount: 
Timestamp: 
"""
application_name = "Bank Simulator"
options = """Options:
1. Create an Account 
2. Money Deposit 
3. Withdraw money 
4. Transfer money 
5. Display Account 
6. Transaction history
7. Check Balance
8. Exit 
"""
accounts = [] 
transactions = []
account_types = ("check-in", "savings", "corporate")
"""
storing account types in list is a major security issue 
the data inside the list can be modified at any time.
mutability -> ability to be modified 
immutability -> they cannot be modified they are constant 
list,dictonary -> mutable data structures 
tuple -> immutable data structure
"""


def find_account(acc_num):
    """Search the accounts list for a matching account_number, return it or None."""
    for acc in accounts:
        if acc["account_number"] == acc_num:
            return acc
    return None


def get_valid_account(prompt="Enter the Account Number: ", exclude=None):
    """
    Keep prompting until the entered account number actually exists.
    'exclude' can be an account number that isn't allowed (e.g. the
    "from" account when picking a "to" account in a transfer), so the
    user can't pick the same account twice.
    Returns the (account_number, account_dict) once a valid one is entered.
    """
    while True:
        acc_num = int(input(prompt))
        if exclude is not None and acc_num == exclude:
            print("This account is already selected elsewhere. Please choose a different account.")
            continue
        acc = find_account(acc_num)
        if acc is None:
            print("Account not found. Please enter an existing account number.")
            continue
        return acc_num, acc


def verify_pin(account, max_attempts=3):
    """Ask for the account's PIN, giving a few tries. Returns True if correct."""
    for attempt in range(max_attempts):
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == account["pin"]:
            return True
        remaining = max_attempts - attempt - 1
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
    print("Too many incorrect attempts. Transaction cancelled.")
    return False


while True: 
    print(application_name+":")
    print(options)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Creating Account: ")
            holder_name = input("Holder's Name: ")
            holder_age = int(input("Holder's Age: "))
            print("Account Type:")
            print("1. Check-In")
            print("2. Savings")
            print("3. Corporate")
            type_choice = int(input("choose the Account Type: "))

            if type_choice < 1 or type_choice > len(account_types):
                print("Invalid account type, defaulting to savings")
                account_type = "savings"
            else:
                account_type = account_types[type_choice-1]

            pin = input("Set a 4-digit PIN: ").strip()

            account_number = len(accounts) + 1
            account = {
                "account_number": account_number,
                "holder_name": holder_name,
                "holder_age": holder_age,
                "account_type": account_type,
                "balance": 0.0,
                "pin": pin
            }
            accounts.append(account)
            print(f"Account created successfully! Account Number: {account_number}")

        case 2:
            print("Money Deposit: ")
            account_number, account = get_valid_account()
            if not verify_pin(account):
                pass
            else:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    account["balance"] += amount
                    transaction_id = len(transactions) + 1
                    transaction = {
                        "transaction_id": transaction_id,
                        "type": "Deposit",
                        "from_account": None,
                        "to_account": account_number,
                        "amount": amount,
                        "timestamp": now_arizona()
                    }
                    transactions.append(transaction)
                    print(f"Deposited {amount} successfully. New balance: {account['balance']}")

        case 3:
            print("Money Withdraw: ")
            account_number, account = get_valid_account()
            if not verify_pin(account):
                pass
            else:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > account["balance"]:
                    print("Insufficient balance.")
                else:
                    account["balance"] -= amount
                    transaction_id = len(transactions) + 1
                    transaction = {
                        "transaction_id": transaction_id,
                        "type": "Withdraw",
                        "from_account": account_number,
                        "to_account": None,
                        "amount": amount,
                        "timestamp": now_arizona()
                    }
                    transactions.append(transaction)
                    print(f"Withdrew {amount} successfully. New balance: {account['balance']}")

        case 4:
            print("Transfer Money: ")
            from_account_number, from_account = get_valid_account("Enter the From account: ")
            if not verify_pin(from_account):
                pass
            else:
                to_account_number, to_account = get_valid_account(
                    "Enter the To account: ", exclude=from_account_number
                )
                amount = float(input("Enter the ammount: "))

                if amount <= 0:
                    print("Transfer amount must be positive.")
                elif amount > from_account["balance"]:
                    print("Insufficient balance.")
                else:
                    # deduct from source, add to destination
                    from_account["balance"] -= amount
                    to_account["balance"] += amount

                    # record the transaction
                    transaction_id = len(transactions) + 1
                    transaction = {
                        "transaction_id": transaction_id,
                        "type": "Transfer",
                        "from_account": from_account_number,
                        "to_account": to_account_number,
                        "amount": amount,
                        "timestamp": now_arizona()
                    }
                    transactions.append(transaction)

                    print(f"Transferred {amount} successfully from Account {from_account_number} "
                          f"to Account {to_account_number}.")
                    print(f"New balance for Account {from_account_number}: {from_account['balance']}")
                    print(f"New balance for Account {to_account_number}: {to_account['balance']}")

        case 5:
            print("Displayig Account: ")
            account_number, account = get_valid_account()
            rows = [
                [
                    account["account_number"],
                    account["holder_name"],
                    account["account_type"],
                    account["holder_age"],
                    account["balance"]
                ]
            ]
            headers = [
                "Account Number",
                "Holder Name",
                "Account Type",
                "Age",
                "Balance"
            ]
            print("Account Details:")
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        case 6:
            print("Transactions: ")
            if not transactions:
                print("No transactions have been made yet.")
            else:
                filter_choice = input(
                    "Show all transactions or filter by account number? (all/account): "
                ).strip().lower()

                if filter_choice == "account":
                    account_number, account = get_valid_account()
                    filtered = [
                        t for t in transactions
                        if t["from_account"] == account_number or t["to_account"] == account_number
                    ]
                    if not filtered:
                        print("No transactions found for this account.")
                    else:
                        rows = [
                            [
                                t["transaction_id"],
                                t["type"],
                                t["from_account"] if t["from_account"] is not None else "-",
                                t["to_account"] if t["to_account"] is not None else "-",
                                t["amount"],
                                t["timestamp"]
                            ]
                            for t in filtered
                        ]
                        headers = ["Transaction ID", "Type", "From Account", "To Account", "Amount", "Date/Time (AZ)"]
                        print(f"Transaction History for Account {account_number}:")
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                else:
                    rows = [
                        [
                            t["transaction_id"],
                            t["type"],
                            t["from_account"] if t["from_account"] is not None else "-",
                            t["to_account"] if t["to_account"] is not None else "-",
                            t["amount"],
                            t["timestamp"]
                        ]
                        for t in transactions
                    ]
                    headers = ["Transaction ID", "Type", "From Account", "To Account", "Amount", "Date/Time (AZ)"]
                    print("All Transactions:")
                    print(tabulate(rows, headers=headers, tablefmt="grid"))

        case 7:
            print("Check Balance: ")
            account_number, account = get_valid_account()
            if verify_pin(account):
                print(f"Account {account_number} Balance: {account['balance']}")

        case 8:
            print("Exiting...")
        case _ : 
            print("Invalid Choice, Try again.")

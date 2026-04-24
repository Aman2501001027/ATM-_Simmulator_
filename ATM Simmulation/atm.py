import data
import storage
from datetime import datetime

def check_balance():
    print(f"\n💰 Current Balance: ₹{data.balance}")

def deposit():
    amount = float(input("Enter amount to deposit: ₹"))
    data.balance += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data.transactions.append(f"{time} - Deposited: ₹{amount}")

    storage.save_data()
    print("✅ Deposit Successful!")

def withdraw():
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > data.balance:
        print("❌ Insufficient Balance!")
    else:
        data.balance -= amount

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        data.transactions.append(f"{time} - Withdrawn: ₹{amount}")

        storage.save_data()
        print("✅ Withdrawal Successful!")

def show_statement():
    print("\n📄 Transaction Statement:")

    if not data.transactions:
        print("No transactions yet.")
    else:
        for t in data.transactions:
            print("-", t)
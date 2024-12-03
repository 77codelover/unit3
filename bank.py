class bank:
    def __init__(self,name,bal=0.0):
        self.name = name
        self.balance = bal

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("cannot withdraw:")
        else:
            self.balance-=amount
            return self.balance
name = input("Enter Name:")


b = bank(name)
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        amount = float(input("Enter the amount to deposit: "))
        new_balance = b.deposit(amount)
        print(f"Amount deposited successfully. New balance: {new_balance}")
    elif ch == 2:
        amount = float(input("Enter the amount to withdraw: "))
        new_balance = b.withdraw(amount)
        if new_balance is not None:
            print(f"Amount withdrawn successfully. New balance: {new_balance}")
    elif ch == 3:
        print(f"Current balance: {b.balance}")
    elif ch == 4:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.")
class BankAccount:
    def __init__(self,account_number,name,account_type,balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited amount: ", amount)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        print("Withdraw amount: ", amount)
    def display(self):
        print("Name:", {self.name})
        print("Account Number:", {self.account_number})
        print("Account Type:", {self.account_type})
        print("Balance:", {self.balance})
account_number = int(input("Enter account number: "))
name = input("Enter name: ")
account_type = input("Enter account type: ")
member = BankAccount(account_number,name,account_type,0)

while True:
    member.display()
    transaction=int(input("Enter 1 to deposit, 2 to withdraw, 3 to quit: "))
    if transaction==1:
        member.deposit(int(input("Enter the amount: ")))
    elif transaction==2:
        member.withdraw(int(input("Enter the amount: ")))
    elif transaction==3:
        print("Thank you for your time")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          # public
        self.__balance = balance    # private

    # getter
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive!")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount


account = BankAccount("Mohit", 100)
account.deposit(50)
print(account.get_balance())   # 150

account.withdraw(1000)         # Insufficient funds!
account.__balance = 999999     # ignored (name mangling)
print(account.get_balance())   # still 150 — object is protected
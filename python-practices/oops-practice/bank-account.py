
from abc import ABC, abstractmethod

# from abc import ABC, abstractmethod


class account(ABC):
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    
    def get_balance(self):
        return self.__balance
    
    def deposit_balance(self, amount):
        self.__balance += amount


    def account_type(self):
        pass

class saving_acct(account):

    def account_type(self):
        account_type = "saving"
        return account_type
    


person1 = saving_acct("prashant",2000)
person1.deposit_balance(3000)

print(person1.get_balance())
print(person1.account_type())



    


    




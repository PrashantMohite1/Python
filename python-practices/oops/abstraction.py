from abc import ABC, abstractmethod

# Abstract base class — a blueprint, NOT a usable object on its own.
# It says WHAT every payment must do (pay), but not HOW.
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass          # no body — each subclass MUST provide its own

    # a normal (concrete) method — shared by all subclasses
    def receipt(self, amount):
        print(f"Receipt: paid {amount} successfully.")


# Concrete class 1 — hides the "how" of card processing
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card...")
        self.receipt(amount)


# Concrete class 2 — different internal details, same interface
class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using UPI...")
        self.receipt(amount)


# The user only needs to know .pay() — the internals are hidden (abstracted away)
def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(CreditCardPayment(), 500)
checkout(UpiPayment(), 200)

# Payment()  ->  TypeError: Can't instantiate abstract class Payment
#               with abstract method pay

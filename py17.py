from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class: CreditCard
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Credit Card.")

# Concrete class: UPI
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI (e.g., Google Pay, PhonePe).")

# Instantiate and demonstrate
payment1 = CreditCard()
payment2 = UPI()

# Calling the pay method
payment1.pay(1500)
payment2.pay(500)

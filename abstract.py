#Create an abstract class PaymentGateway with abstract methods pay() and refund(). Implement two subclasses: CreditCardPayment and PayPalPayment. Demonstrate calling their methods.
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
	@abstractmethod
	def pay(self, amount):
	 pass

	@abstractmethod
	def refund(self,amount):
	 pass

class CreditCardPayment(PaymentGateway):
	def __init__(self,card_number,holder_name):
		self.card_number = card_number
		self.holder_name = holder_name

	def pay(self,amount):
		print(f"Processing Credit Card payment of Rs.{amount} for {self.holder_name} (Card: ****{self.card_number[-4:]}).")

	def refund(self,amount):
		print(f"Refunding Rs.{amount} back to Credit Card ****{self.card_number[-4]}.")

class PayPalPayment(PaymentGateway):
	def __init__(self,email):
		self.email = email

	def pay(self,amount):
		print(f"Processing PayPal payment of Rs.{amount} via account: {self.email}.")

	def refund(self,amount):
		print(f"Refunding Rs.{amount} to PayPal account: {self.email}.")

if __name__ == "__main__":
	print("--- Testing Credit Card Payment ---")
	cc_payment = CreditCardPayment("123456789","Nirajan")
	cc_payment.pay(150.00)
	cc_payment.refund(100.00)

	print("\n-- Testing PayPal Payment ---")
	paypal_payment = PayPalPayment("nirajanaryal@example.com")
	paypal_payment.pay(100.00)
	paypal_payment.refund(50.00)

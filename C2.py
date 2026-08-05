'''C2.Create a custom exception `InvalidAgeError` that stores the invalid age value as an attribute. Write a function `check_age(age)` that raises this error if age is less than 0 or greater than 120.'''
class InvalidAgeError(Exception):
	def __init__(self,age):
		self.age = age
		super().__init__(f"Invalid age {age}. Age must be greater than 0 and less than 120.")

def check_age(age):
	if age<0 or age>120:
		raise InvalidAgeError(age)
	else:
		print("Age =",age)

try:
	age = int(input("Enter any age:"))
	check_age(age)

except InvalidAgeError as e:
	print("Error occured ",e)
	print("Invalid age entered :",e.age)

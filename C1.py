'''C1.Create a custom exception class called 'NegativeNumberError' that inherits from "Exception'. Write a function that raises it if a user enters a negative number.'''
class NegativeNumberError(Exception):
	pass

def check_num(num):
	if num<0:
		raise NegativeNumberError("Negative number not allowed.")
	else:
		print("You entered =",num)

try:
	number = int(input("Enter a number:"))
	check_num(number)

except NegativeNumberError as e:
	print("Error found ",e)

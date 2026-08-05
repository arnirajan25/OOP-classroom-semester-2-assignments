'''Write a program that asks the user to enter a number and divides 100 by it. Use `try/except` to catch `ZeroDivisionError` if they enter 0.'''

try:
	number = int(input("Enter a number:"))
	result = 100 / number
	print("Result =", result)
except ZeroDivisionError:
	print("Error: You cannot divide by zero.")


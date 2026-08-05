'''A5.Modify A1 so that a 'finally' block always prints "Program finished running." regardless of whether an error occurred.'''

try:
	number = int(input("Enter a number: "))
	result = 100/number
	print("Result =", result)

except ZeroDivisionError:
	print("Error: You cannot divide by zero.")

finally:
	print("Program finished running.")

'''A2.Write a program that converts user input to an integer using 'int().Catch the 'ValueError' that occurs if they type letters instead of numbers.'''

try:
	number = int(input("Enter an integer: "))
	print("You entered:", number)
except ValueError:
	print("Error: Please enter a valid integer.")

'''A4.Modify A2 so that after the `except block, add an 'else block that prints "Conversion successful!" only if no error occurred.'''

try:
	number = int(input("Enter an integer: ")) 
	print("You entered:", number)
except ValueError:
	print("Error: Invalid input.")
else:
	print("Conversion successful!")

'''A3.Write a program with a list of 5 items. Ask the user for an index and print the item at that index. Catch the 'IndexError if the index is out of range.'''

items = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
try:
	index = int(input("Enter index (0-4): ")) 
	print("Item:", items[index])
except IndexError:
	print("Error: Index is out of range.")

'''B1. Write a function 'safe divide(a, b) that catches both 'ZeroDivisionError and TypeError in a single 'except' block (e.g., handle both dividing by zero and passing a string instead of a number).'''
def safe_divide(a,b):
	try:
		result = a/b
		print("Result",result)
	except(ZeroDivisionError,TypeError):
		print("Error. Cannot divide by zero or by a non-integer value.")


safe_divide(10,2)
safe_divide(5,0)
safe_divide(7,"a")
safe_divide(8,"1")


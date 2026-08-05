'''*B2.* Write a function that catches an exception, prints "Logging error...", and then re-raises the same exception using 'raise'.'''
def divide(a,b):
	try:
		result = a/b
		print("Result =",result)
		return result

	except Exception:
		print("Logging Error...")
		raise

try:
	print(divide(10,0))
except Exception as e:
	print("Error found ",e)

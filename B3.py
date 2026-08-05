'''*B3.* Call the function from B2 inside a 'try/except block from the caller's side, and confirm that the caller is still able and handle the re-raised exception.'''
def divide(a,b):
	try:
		return a/b

	except Exception:
		print("Logging Error...")
		raise


try:
	result = divide(10,2)
	print("Result = ",result)
	res = divide(8,0)
	priint("Another result = ",res)

except Exception as e:
	print("Caller handled the exception ",e)


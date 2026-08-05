#(Single Inheritance) Write a program with a Parent class containing a method show_message(). Create a Child class that that inherits from Parent and adds its own method. Demonstrate calling both methods.
class Parent:
	def show_message(self):
		print("Hello form Parent Class.")

class Child(Parent):
	def show_info(self):
		print("Hello from Child Class.")

c1 = Child()
print("\nInherited method:")
c1.show_message()
print("\nChild's Own method:")
c1.show_info()

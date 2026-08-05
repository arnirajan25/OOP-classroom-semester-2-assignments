#(slots)Write a Person class with _slots = ["name', 'age']. Show that adding attributes outside slots raises an error. Compare memory usage with a normal class.
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
	p = Person("Nirajan", 20)
	print(f"Created person: {p.name}, Age: {p.age}")
	print("\nAttempting to add 'email' attribute...")
try:
        p.email = "nirajan@example.com"
except AttributeError as e:
	print(f"Error Caught successfully: {e}")

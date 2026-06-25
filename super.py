#[super()Function] Write a Person class with attributes name and age. Create a Student subclass that adds roll_number. Use super() to call the parent constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)

s = Student("Nirajan",20,10)
s.display()

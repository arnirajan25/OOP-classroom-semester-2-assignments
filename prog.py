'''class Dog:
   name="Rover"
   print( "Hello",name)

d1=Dog()
print (d1.name)


class Student:
    def __init__():
        print("Hello")
    def __init__(self, Name, LastName):
        self.name = Name
        self.last_name = LastName


s1=Student("Nirajan","Aryal")
s2=Student("Suhag","Adhiakri")

print (s1.name)
print(s1.last_name)
print(s2.name+ " " + s2.last_name)

class BCS:
    def __init__(self, Name, LastName):
        self.name = Name
        self.last_name = LastName

    def info(self):
        print("Name:",self.name,"Last Name:",self.last_name)

class Student(BCS):
    def purpose(self):
        print(self.name,"studies BCS")

s1=Student("Nirajan","Aryal")
s1.info()
s1.purpose()

class A:   
    def info(self):
        print("Nirajan")

class B(A):
    def purpose(self):
        print("studies BCS")

class C(A):
    def hobby(self):
        print("likes programming!")

class D(B,C):
    pass

a=D()
a.info()
a.purpose()
a.hobby()
print(D.mro())


from Area import Area
class Rectangle(Area):
    def __init__(self, length, breadth):
        self.length = 10
        self.breadth = 11
    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Square(Area):
    def __init__(self, side):
        self.length = 10
        self.breadth = 9

    def perimeter(self):
        return 4 * self.length

class Circle:
    def __init__(self, radius):
        self.radius = 5

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

r1=Rectangle(10,11)
print("Area of Rectangle:",r1.area())
print("Perimeter of Rectangle:",r1.perimeter())
s1=Square(10)
print("Area of Square:",s1.area())
print(
"Perimeter of Square:",s1.perimeter())
c1=Circle(5)
print("Area of Circle:",c1.area())
print("Perimeter of Circle:",c1.perimeter())


class Animal: pass
class Dog(Animal): pass

d=Dog()
print(isinstance(d,Dog)) 
print(isinstance(d,Animal)) 
print(issubclass(Dog,Animal)) 

class Bird:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Bird Name: {self.name}")

class FlyMixin:
    def fly(self):
        print(f"{self.name} is flying!")

class SwimMixin:
    def swim(self):
        print(f"{self.name} is swimming!")

class Duck(Bird, FlyMixin, SwimMixin):
    def __init__(self, name):
        super().__init__(name)

d= Duck("hello Duck")
d.display()
d.fly()
d.swim()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Nirajan", 20)
print(p.__dict__)  # Output: {'name': 'Nirajan', 'age': 20} 

#Create an abstract class PaymentGateway with abstract methods pay() and refund(). Implement two subclasses: CreditCardPayment and PayPalPayment. Demonstrate calling their methods.
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
     pass

    @abstractmethod
    def refund(self,amount):
     pass

class CreditCardPayment(PaymentGateway):
        def __init__(self,card_number,holder_name):
                self.card_number = card_number
                self.holder_name = holder_name

        def pay(self,amount):
                print(f"Processing Credit Card payment of Rs.{amount} for {self.holder_name} (Card: ****{self.card_number[-4:]}).")

        def refund(self,amount):
                print(f"Refunding Rs.{amount} back to Credit Card ****{self.card_number[-4]}.")

class PayPalPayment(PaymentGateway):
        def __init__(self,email):
                self.email = email

        def pay(self,amount):
                print(f"Processing PayPal payment of Rs.{amount} via account: {self.email}.")

        def refund(self,amount):
                print(f"Refunding Rs.{amount} to PayPal account: {self.email}.")

if __name__ == "__main__":
    print("--- Testing Credit Card Payment ---")
    cc_payment = CreditCardPayment("123456789","Nirajan")
    cc_payment.pay(150.00)
    cc_payment.refund(100.00)

    print("\n-- Testing PayPal Payment ---")
    paypal_payment = PayPalPayment("nirajanaryal@example.com")
    paypal_payment.pay(100.00)
    paypal_payment.refund(50.00)
    
#try:
 #   num=int(input("Enter a number: "))
  #  res=10/num
   # print (res)
#except(ValueError,ZeroDivisionError) as e:
 #   print("Caught an exception:", type(e).__name__)
def divide(a,b):
    try: 
        return a/b
    except ZeroDivisionError as e:
        print("Logging: Division by zero attempted.")
        raise

    try:
        result=divide(10,0)
    except ZeroDivisionError:
        print("Handled again in outer block")

import mymodule

print(mymodule.greet("Nirajan"))
print(mymodule.add(10,9))


#random module
import random
print("Random Examples:")
print(random.randint(1,10))
print(random.choice(["apple","banana","cherry"]))
numbers=[1,2,3,4,5]
random.shuffle(numbers)
print(numbers)
print()

#datetime module
import datetime
print("Date and Time Examples:")
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now())
future=datetime.datetime.today() + datetime.timedelta(days=7)
print("Date after 7 days:",future)
print()

#os module
import os
print("OS Examples:")
print("Current working directory:",os.getcwd())
print("Files in current directory:",os.listdir())
print()

#sys module
import sys
print("Sys Examples:")
print("Python version:",sys.version)
print("Platform:",sys.platform)
print("Command line arguments:",sys.argv)
print("Module search path:",sys.path)

def divide(a,b):
    try:
        return a/b
    except (ZeroDivisionError,TypeError) as e:
        print(f"Zero attempted:{e}")
        raise

try:
    divide(10,0)
except ZeroDivisionError:
    print("Handled:Cannot divide by zero")

try:
    divide(10,"n")
except TypeError:
    print("Handled: Invalid type for division")


class MyCustomError(Exception):
    pass

def check_age(age):
    if age<0:
        raise MyCustomError("Age cannot be negative!")
    return age

try:
    check_age(-1)
except MyCustomError as e:
    print(f"Caught: {e}")


class MyConnection:
    def __enter__(self):
        print("Establishing connection")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Terminating connection")

with MyConnection as conn:
    print("Using connection")


s="Hello Nirajan"
print(s[5:13:1])
print(s[::-1])

for i in range(10):
    print(f"Stop only {i}:",i)
#range (start,stop,step) = range(1,10,2) = 1,3,5,7,9


A={1,2,3,4}
B={3,4,5,6}
A.add(10)
A.remove(3)
A.discard(8)
print("Set A:",A)
print("Set B:",B)
print("Union: ",A|B)
print("Intersection: ",A&B)
print("Difference: ",A-B)
print("Symmectric Difference: ",A^B)


A={
    "name":"Nirajan",
    "age":20,
    "status":"Ongoing",
    "Hobby":["Programming","Gaming","Reading"],
    "Interests":{ "Sports":["Football","Cricket","Basketball"],
                  "Music":["Pop","Rock","Classical"]}
}
C ={"work":"Classified"}
B={"contact":9999999999,"email":"nirajanaryal@example.com"}
A.update(C)
print(A)
A["age"]=21
print(A)



squares=[x**2 for x in range(1,6)]
print("Square list:", squares)

numbers=[1,2,3,4,5,6,7,8,9,10]
even=[n for n in numbers if n%2==0]
print("Even numbers:", even)

label=["Even" if n%2==0 else "Odd" for n in numbers]
print("Number Labels",label)

a=str(input("Enter a string: "))
b=a.split()
print("List of the string:",b)

'''

c="I love playing sports, I can play football until my lungs give out."
d=c.rpartition("play")
print(d)

e="Hello, my name is Nirajan."
f=e.title()
print(f)
g=e.swapcase()
print(g)

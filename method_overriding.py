#(Method Overriding) Create a Vehicle class with a method move(). Derive a Car class that overrides move() to print "Car is driving". Show how overriding works.
class Vehicle:
    def move(self):
        print("The vehicle is moving in some way.")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

print("Creating a Car Instance")
c1 = Car()
c1.move() 

print("\nCreating a Base Vehicle Instance")
v1 = Vehicle()
v1.move()

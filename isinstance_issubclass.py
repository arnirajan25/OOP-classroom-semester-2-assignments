'''isinstance() and issubclass() 
Write a program with classes Animal and Dog. Create a Dog object and check:
1.if it is an instance of Dog and Animal using isinstance()
2.if Dog is a subclass of Animal using issubclass()
'''
class Animal: pass
class Dog(Animal): pass

d=Dog()
print(isinstance(d,Dog)) 
print(isinstance(d,Animal)) 
print(issubclass(Dog,Animal)) 

'''E3.Modifyinit.py in 'mathpackage/ to import add' and 'power directly, so they can be used as 'mathpackage.add(...) and 'mathpackage.power(...) without referencing 'basic or advanced.'''

import mathpackage

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", mathpackage.add(a, b))
print("Power =", mathpackage.power(a, b))

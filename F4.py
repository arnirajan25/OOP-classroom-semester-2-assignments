'''F4.Use the 'random' module to simulate rolling a 6-sided dice 5 times and print each result.'''
import random
print("Random Examples:")
print(random.randint(1,10))
print(random.choice(["apple","banana","cherry"]))
numbers=[1,2,3,4,5]
random.shuffle(numbers)
print(numbers)
print()

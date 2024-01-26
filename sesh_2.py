# Created by Kaelen Cook
# Jan 2024
import math, random

# print sum of 2 floating points
def float_sum(a, b):
    print("a: " + str(a))
    print("b: " + str(b))
    x = a + b
    return x

# difference of 2 ints
def int_difference(a, b):
    print("a: " + str(a))
    print("b: " + str(b))
    x = a - b
    return x

# product of float * int
def product(a, b):
    print("a: " + str(a))
    print("b: " + str(b))
    x = a * b
    return x

a = random.uniform(-10, 10)
b = random.uniform(-10, 10)
c = random.randint(-10, 10)
d = random.randint(-10, 10)

x = float_sum(a, b)
print(x)
print(f"type: {type(x)}")
y = int_difference(c, d)
print(y)
print(f"type: {type(y)}")
z = product(a, c)
print(z)
print(f"type: {type(z)}")
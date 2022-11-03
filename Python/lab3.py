# 1. calculator area
# 2. is palindrom
# 3. list split to 2 list event and odd
# 4. count big and small leters in string
# 5. facturiel
# 6. list with 15 to list(set)

import math
import random

def triangle_area(a, ha):
    return a * ha / 2

def square_area(a):
    return a * a

def circle_area(r):
    return math.pi * r**2

def calculator_area():
    figure_type = input("Figure type: ")
    match figure_type:
        case "Triangel":
            a, ha = map(int ,input("Sizes: ").split())
            print("Triangle area is: {0}".format(triangle_area(a,ha)))
        case "Square":
            a = int(input("Sizes: "))
            print("Square area is: {0}".format(square_area(a)))
        case "Circle":
            r = int(input("Sizes: "))
            print("Cicle area is: {0}".format(circle_area(r)))
        case _:
            "No valid figure type!"

def is_palidrom(string):
    return string == string[::-1]

def list_split(list_var):
    list_even, list_odd = [i for i in list_var if i % 2 == 0], [i for i in list_var if i % 2 != 0]
    print("List: {0}".format(list_var))
    print("Even list: {0}".format(list_even))
    print("Odd list: {0}".format(list_odd))

def lagre_small_leters(string):
    small, large = sum(1 for c in string if c.islower()), sum(1 for c in string if c.isupper())
    print("small: {small}, large: {large}".format(small = small, large =large))

def facturiel(n):
    return math.prod([i for i in range(2, n+1)]) if n >= 1 else "Wrong input!"

def list_to_setlist(list_var):
    return list(set(list_var))

# calculator_area()

# string = input("Input: ")
# print(is_palidrom(string))

list = list(map(int, input("List: ").split()))
print(list)
list_split(list)

# string = input("Sting: ")
# lagre_small_leters(string)

# n = int(input("N: "))
# print(facturiel(n))

# print(list_to_setlist([random.randint(0, 100) for _ in range(15)]))
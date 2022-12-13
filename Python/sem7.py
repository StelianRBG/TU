import math

def input_number():
    n = int(input("N: "))
    if n < 1000 or n > 2000:
        raise ValueError
    return n

def check_number():
    while True:
        try:
            n = input_number() % math.pi
            n = str(n).split('.')
            if '7' in n[1][:5]:
                return True
        except ValueError:
            print('Number must be between 1000 and 2000')     

def number_dict():
    n = 0
    while n < 1:
        n = int(input("N: "))
    return {key: (n-key+1)**2 for key in range(n, 0, -1)}


# print(check_number())

print(number_dict())
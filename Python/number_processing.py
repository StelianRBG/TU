import random

# Function witch return is the number even and sum of its digits
def number_processing(number):
    print("Number: " + str(number))
    is_even = True if number % 2 == 0 else False
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    print("Sum of digits of number: " + str(sum))
    print("Is number even: " + str(is_even))

number = random.randint(0, 1000)
number_processing(number)

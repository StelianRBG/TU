# 1. calculator valute (ot, stojnost, do) лев/долар/евро/паунд
# 2. клакулкатор от грдус <-> радиан
# 3. 2 в 16 код
# 4. месец и година -> 24 е понеделник
# 5. Текст от клавиатуратра -> малки главни букви 
# 6. Цяло полужително число -> корен от това число + изключение за -, 0

from math import pi
from datetime import datetime

def cur_calculator():
    start_cur = input("Start curency: ")
    value = float(input("Value: "))
    result_cur = input("Result curency: ")

    from_dolar = {"bgn": 1.88, "euro": 0.96, "pound": 0.82, "dolar": 1}

    try:
        return str(value / from_dolar [start_cur] * from_dolar[result_cur]) + " " + result_cur
    except:
        return "Wrong curency input"

def deg_to_radian():
    value = float(input("Value: "))
    result_cur = input("Result curency: ")
    multi = pi/180
    match result_cur:
        case "deg":
            return str(value / multi) + " deg"
        case "rad":
            return str(value * multi) + " rad"
        case _ :
            return "Wrong input"

def binary_to_hex():
    return hex(int(input(), 2))

def check_24_is_monday():
    return datetime(int(input("Year: ")), int(input("Mouth: ")), 24).weekday() == 0

def small_big_leters():
    text = input()
    small = [c for c in text if c.islower()]
    big = [c for c in text if c.isupper()]
    print("Small: ")
    print(small, len(small))
    print("Big: ")
    print(big, len(big))

def sqrt():
    n = int(input("Number: "))
    if n <= 0:
        raise ValueError
    return n ** (1/2)
 
# print(cur_calculator())
# print(deg_to_radian())
# print(binary_to_hex())
# print(check_24_is_monday())
# small_big_leters()

print(sqrt())

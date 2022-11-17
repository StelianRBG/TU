#1. цяло число в два куртежа четни и нечетни
#2. списък със случайни числа между всеки 2 сбора им

from random import randint

def number_to_tuples():
    number = int(input("Number: "))
    t_even, t_odd = [], []
    for i in range(number):
        if i % 2 == 0:
            t_even.append(i)
        else:
            t_odd.append(i)
    print("Even: {t_even}\n\nOdd: {t_odd}".format(t_even = tuple(t_even), t_odd = tuple(t_odd)))

def rand_list():
    list_size = int(input("Count of list elements: "))
    list = [randint(0, 100) for _ in range(list_size)]
    print(list)
    for i in range(0, 2*list_size-2, 2):
        list.insert(i+1, list[i] + list[i+1])
    print(list)

def resize_list():
    list1 = list(input("String: "))
    while len(list1) > 2:
       list1 = list1[1:-1]
    print(list1[0])

# number_to_tuples()
# rand_list()
resize_list()


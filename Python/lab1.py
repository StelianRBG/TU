import random

def random_list():
    n = int(input("N: "))
    my_list = [random.randint(0, 100) for i in range(n)]
    return my_list


def list_sum_avg():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    sum_of_list = sum(my_list)
    print("Sum = " + str(sum_of_list))
    print("Avg = " + str(sum_of_list/7))

def is_palindrom():
    n = input("N: ")
    my_list = list(n)
    my_list.reverse()
    r = "".join(my_list)
    return r == n
# print(random_list())
# list_sum_avg()
# print(is_palindrom())
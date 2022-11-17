# 1. x, o, y Всички подредби без повтаряне
# 2. Подредба в лист Монотонно намаляваща/ Монотонно растяща/ Смесица
# 3. 4 цифрено число Обръщаме това число и го обръщаме с първото поверяваме за дали резултата е палиндром ако е спира ако не е ново въвеждане
# 4. Речник от главните и малките букви

from itertools import permutations

def permutation():
    list1 = ['x', 'y','z', 'o']
    for i in list1:
        list2 = [j for j in list1 if j != i]
        for j in list2:
            list3 = [k for k in list2 if k != j]
            for k in list3: 
                result = [i, j, k]
                list4 = [l for l in list3 if l != k]
                for l in list4:
                    print(result + [l])
    # easy way
    # print(list(permutations(list1,4)))

def list_order(list1):
    # count max and orders
    maxs, mins = 0, 0
    for i in range(1,len(list1)):
        if list1[i] > list1[i-1]:
            maxs += 1
        else:
            mins +=1
    # check maxs and mins
    if maxs == len(list1) - 1:
        return "Монотонно растяща редица"
    elif mins == len(list1) - 1:
        return "Монотонно намаляваща редица"
    else:
        return "Неопределена редица"

def is_palindrom(n):
    return str(n) == str(n)[::-1]

def number_check():
    while True:
        n = input("Number: ")
        reverse_n = n[::-1]
        if is_palindrom(int(n) + int(reverse_n)):
            return True

def text_process(text):
    small, large = sum(1 for c in text if c.islower()), sum(1 for c in text if c.isupper())
    return {"small": small, "large": large}
        


# permutation()

# list1 = list(map(int, input("List: ").split()))
# print(list_order(list1))

# print(number_check())

string = input("Sting: ")
print(text_process(string))
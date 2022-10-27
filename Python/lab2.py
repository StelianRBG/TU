def string_to_dict():
    string = input("String: ")
    result = {}
    for i in string:
        if i not in result.keys():
            result[i] = string.count(i)      
    print(result)

def number_to_dict():
    number = int(input("Number: "))
    new_list = [i for i in range(1, number+1)]
    new_list.reverse()
    result = {i: new_list[i-1] for i in range(1, number+1) }
    print(result)

def calculator(a, b, operator):
    match operator:
        case "+":
            return add(a, b)
        case "-":
            return sub(a, b)
        case "*":
           return  multi(a, b)
        case "/":
            return div(a, b)
        case _:
            return "This operator is not define!"
        
def add(a, b):
    return('{a} + {b} = {c}'.format(a = a, b = b, c = a + b))

def sub(a, b):
    return('{a} - {b} = {c}'.format(a = a, b = b, c = a - b))

def multi(a, b):
    return '{a} * {b} = {c}'.format(a = a, b = b, c = a * b)

def div(a, b):
    return '{a} / {b} = {c}'.format(a = a, b = b, c = a / b)

def list_to_zero(list, n):
    for i in range(len(list)):
        if list[i] > n:
            list[i] = 0
    print(list)

# string_to_dict()

# number_to_dict()

# a, b, operator = input().split()
# a, b = int(a), int(b)
# print(calculator(a, b, operator))

list_to_zero([1,2,3,4,5,6,7], 4)

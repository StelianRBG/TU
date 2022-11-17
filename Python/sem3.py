# betwen 0 5000 % 8 and % 6
def between_0_500():
    return [i for i in range(0, 5001) if i % 6 == 0 and i % 8 == 0]

# 3 input numbers -> mediana
def mediana():
    list1 = []
    while len(list1) != 3:
        list1 = list(map(int, input("Numbers: ").split()))
    list1.sort()
    return(list1[1])

# print * 
def stars():
    n = int(input("Number: "))
    for i in range(1, 2*n ):
        if i > n :
            print((2*n-i) * '*')
        else:
             print(i * '*')

def triangle():
    list1 = list(map(int, input("Numbers: ").split()))
    list1.sort()
    if list1[2] > list1[0] + list1[1]:
        return "Invalid"
    elif list1[0] == list1[1] == list1[2]:
        return "Равностранен"
    elif list1[0] == list1[1] or list1[0] == list1[2] or list1[1] == list1[2]:
        return "Равнобедрен"
    else:
        return "Разностанен"

def input_numbers():
    n = int(input("Count of numbers: "))
    list1 = [int(input("Number: ")) for _ in range(n)]
    list1.sort()
    return list1[n-1]



# print(between_0_500())
# print(mediana())
# stars()
# print(triangle())
print(input_numbers())



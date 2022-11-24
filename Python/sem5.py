def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# def is_prime():
#     n = 37
#     for i in range(2, n):
#         if n % i != 0:
#             break
#     else:
#         print("Is Prime")

# print(is_prime(37))
# print(is_prime(34))


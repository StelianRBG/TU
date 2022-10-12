import decimal

# fuction to get pi with specific precision n
def get_pi_leibniz(precision):
    decimal.getcontext().prec = precision + 1
    pi_val = decimal.Decimal(0)
    for i in range(100000):
        pi_val += (-1)**i  * decimal.Decimal(1) / (2 * i + 1)
    return 4 * pi_val

# function to get number!
def fact(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

# function to get sin of specific angle
def sin_x(angle):
    sin_x_val = 0
    pi  = get_pi_leibniz(10)
    x = angle % 360 * pi / 180
    for i in range(10):
        sin_x_val += (-1)**i * x**(2*i+1) / fact(2 * i + 1)
        
    return round(sin_x_val, 2)

# input and return result
precision = int(input('Input precision of pi: '))
print("pi = " + str(get_pi_leibniz(precision)))
angle = int(input('Input angle to find it sin: '))
print("sin({0}) = ".format(angle) + str(sin_x(angle)))
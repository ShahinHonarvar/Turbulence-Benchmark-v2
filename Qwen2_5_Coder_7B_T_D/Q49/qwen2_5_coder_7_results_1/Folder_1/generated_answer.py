import math

def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 91):
        fib.append(fib[-1] + fib[-2])
    target = fib[90]
    decimal = int(binary_str, 2)
    return decimal % target == 0
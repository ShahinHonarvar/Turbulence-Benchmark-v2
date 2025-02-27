from math import sqrt

def is_fibonacci(n):
    x = 5 * n * n
    return int(sqrt(x + 4) % 1 == 0) * int(sqrt(x - 4) % 1 == 0)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def get_138th_fibonacci():
    fib_a, fib_b = (0, 1)
    for _ in range(138):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    return fib_a

def if_decimal_is_divisible(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % get_138th_fibonacci() == 0
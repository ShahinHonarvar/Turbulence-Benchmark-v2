import math

def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_48th = fibonacci(48)
    decimal_value = binary_to_decimal(bin_str)
    return decimal_value % fib_48th == 0
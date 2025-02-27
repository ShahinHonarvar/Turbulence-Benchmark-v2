from math import sqrt

def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib77 = fibonacci(77)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib77 == 0
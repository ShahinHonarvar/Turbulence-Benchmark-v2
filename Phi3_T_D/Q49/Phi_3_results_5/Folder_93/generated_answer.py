import math

def decimal_from_binary_str(binary_str):
    return int(binary_str, 2)

def fibonacci_modulo(n, modulo):
    a, b = (0, 1)
    for _ in range(n):
        a, b = ((a + b) % modulo, (a + 2 * b) % modulo)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = decimal_from_binary_str(binary_str)
    fibonacci_number = fibonacci_modulo(59, decimal)
    return decimal % fibonacci_number == 0
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci(39) == 0

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
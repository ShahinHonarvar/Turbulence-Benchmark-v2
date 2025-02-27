from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    ninth_fibonacci_number = fibonacci(8)
    return decimal_integer % ninth_fibonacci_number == 0
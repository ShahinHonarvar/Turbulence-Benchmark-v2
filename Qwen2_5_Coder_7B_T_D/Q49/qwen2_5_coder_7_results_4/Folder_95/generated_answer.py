from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_168 = fibonacci(168)
    return decimal_number % fib_168 == 0
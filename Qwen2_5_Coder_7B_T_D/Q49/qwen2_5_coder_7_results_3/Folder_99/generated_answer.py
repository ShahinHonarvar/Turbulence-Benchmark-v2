from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_109 = fibonacci(109)
    return decimal % fib_109 == 0
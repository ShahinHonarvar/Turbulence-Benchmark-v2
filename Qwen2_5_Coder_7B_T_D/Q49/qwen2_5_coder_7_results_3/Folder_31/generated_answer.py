from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    fib_69 = fibonacci(69)
    return decimal_num % fib_69 == 0
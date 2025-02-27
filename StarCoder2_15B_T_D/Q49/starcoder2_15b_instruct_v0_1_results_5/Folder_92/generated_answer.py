from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    nth_fibonacci_number = fib(decimal_integer)
    return decimal_integer % nth_fibonacci_number == 0
from itertools import islice

def if_decimal_is_divisible(binary_str):
    fibonacci_185th = next(islice(fib(), 184, None))
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_185th == 0

def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)
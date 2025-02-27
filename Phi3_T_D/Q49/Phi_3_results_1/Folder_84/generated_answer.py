def if_decimal_is_divisible(binary_string):
    fib_196 = _fib_nth(196)
    decimal = int(binary_string, 2)
    return decimal % fib_196 == 0

def _fib_nth(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a
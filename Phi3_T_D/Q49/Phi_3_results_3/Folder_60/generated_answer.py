def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_str):
    fib_seq = fib()
    for _ in range(108):
        next(fib_seq)
    fib_108 = next(fib_seq)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_108 == 0
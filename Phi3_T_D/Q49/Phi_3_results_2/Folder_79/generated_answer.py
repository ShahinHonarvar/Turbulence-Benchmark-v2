def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_str):
    fib = fibonacci()
    for _ in range(12):
        next(fib)
    target_fib = next(fib)
    decimal = int(binary_str, 2)
    return decimal % target_fib == 0
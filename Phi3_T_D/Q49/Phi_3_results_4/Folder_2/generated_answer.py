def if_decimal_is_divisible(binary_str):

    def fibonacci_125th():
        a, b = (0, 1)
        for _ in range(125):
            yield a
            a, b = (b, a + b)
    fib_125th = list(fibonacci_125th())[-1]
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_125th == 0
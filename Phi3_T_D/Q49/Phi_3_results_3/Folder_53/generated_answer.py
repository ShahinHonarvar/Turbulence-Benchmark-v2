def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_64 = fib(64)
    return decimal_val % fib_64 == 0
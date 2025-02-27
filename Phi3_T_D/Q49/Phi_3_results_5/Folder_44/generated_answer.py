def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fib159 = fib(159)
    return decimal_int % fib159 == 0
def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_100th = fib(100)
    return decimal_value % fib_100th == 0
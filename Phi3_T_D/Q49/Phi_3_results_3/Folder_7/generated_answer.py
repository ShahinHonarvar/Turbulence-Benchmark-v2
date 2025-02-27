def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_160th = fib(160)
    decimal = int(binary_str, 2)
    return decimal % fib_160th == 0
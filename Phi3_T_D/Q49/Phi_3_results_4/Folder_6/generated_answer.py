def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_val = int(binary_str, 2)
    fib_185th = fib(185)
    return decimal_val % fib_185th == 0
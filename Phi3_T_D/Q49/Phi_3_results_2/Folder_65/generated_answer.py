def if_decimal_is_divisible(bin_str):

    def fib():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def golden_ratio(n):
        fib_seq = fib()
        for _ in range(n - 1):
            next(fib_seq)
        return next(fib_seq)
    fib_result = golden_ratio(127)
    decimal_val = int(bin_str, 2)
    return decimal_val % fib_result == 0
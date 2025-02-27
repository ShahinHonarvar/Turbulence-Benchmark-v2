def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_160 = fib(160)
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_160 == 0
def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec_num = int(bin_str[::-1], 2)
    fib_176 = fib(176)
    return dec_num % fib_176 == 0
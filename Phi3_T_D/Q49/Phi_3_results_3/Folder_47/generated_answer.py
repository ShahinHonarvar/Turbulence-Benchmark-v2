def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    dec_num = int(bin_str, 2)
    fib_num = fib(94)
    return dec_num % fib_num == 0
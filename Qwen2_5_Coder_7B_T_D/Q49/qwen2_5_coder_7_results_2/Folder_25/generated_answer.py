def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_19 = fib(19)
    dec_num = int(bin_str, 2)
    return dec_num % fib_19 == 0
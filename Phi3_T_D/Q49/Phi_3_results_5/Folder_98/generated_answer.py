def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def bin_to_dec(bin_str):
        return int(bin_str, 2)
    fib_14 = fib(14)
    dec_value = bin_to_dec(bin_str)
    return dec_value % fib_14 == 0
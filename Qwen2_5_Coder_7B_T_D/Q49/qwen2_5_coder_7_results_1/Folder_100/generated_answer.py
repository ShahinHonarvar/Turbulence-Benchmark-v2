def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_190 = fib(190)
    dec_num = int(binary_str, 2)
    return dec_num % fib_190 == 0
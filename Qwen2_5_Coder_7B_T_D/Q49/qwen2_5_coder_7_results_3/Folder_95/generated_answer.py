def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_168 = fibonacci(168)
    dec_num = int(bin_str, 2)
    return dec_num % fib_168 == 0
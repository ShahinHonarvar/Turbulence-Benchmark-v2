def if_decimal_is_divisible(b_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fourth_fib = fib(4)
    decimal_int = int(b_str, 2)
    return decimal_int % fourth_fib == 0
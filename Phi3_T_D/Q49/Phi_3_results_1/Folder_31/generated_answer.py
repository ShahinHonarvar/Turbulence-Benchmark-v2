def if_decimal_is_divisible(bin_str):

    def fib_69():
        a, b = (0, 1)
        for _ in range(69):
            a, b = (b, a + b)
        return a
    decimal_int = int(bin_str, 2)
    return decimal_int % fib_69() == 0
def if_decimal_is_divisible(bin_str):

    def to_decimal(bin_str):
        return int(bin_str, 2)

    def fib_tenth():
        a, b = (0, 1)
        for _ in range(10):
            a, b = (b, a + b)
        return a
    decimal_val = to_decimal(bin_str)
    return decimal_val % fib_tenth() == 0
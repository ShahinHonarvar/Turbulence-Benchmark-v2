def if_decimal_is_divisible(bin_str):

    def fib_199():
        a, b = (0, 1)
        for _ in range(199):
            a, b = (b, a + b)
        return a
    decimal = int(bin_str, 2)
    return decimal % fib_199() == 0
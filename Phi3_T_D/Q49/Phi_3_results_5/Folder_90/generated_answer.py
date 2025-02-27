def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_177 = fib(177)
    decimal = int(bin_str, 2)
    return decimal % fib_177 == 0
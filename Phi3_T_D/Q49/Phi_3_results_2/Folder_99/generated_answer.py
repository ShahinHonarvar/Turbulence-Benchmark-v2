def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n = int(bin_str, 2)
    fib_109 = fib(109)
    return n % fib_109 == 0
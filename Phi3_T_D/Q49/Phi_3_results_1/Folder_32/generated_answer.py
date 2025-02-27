def if_decimal_is_divisible(binary_string):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_178 = fib(178)
    decimal_int = int(binary_string, 2)
    return decimal_int % fib_178 == 0
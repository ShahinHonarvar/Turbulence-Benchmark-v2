def if_decimal_is_divisible(binary):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary, 2)
    check_fib = fib(188)
    return decimal % check_fib == 0
def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_144th = fib(144)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_144th == 0
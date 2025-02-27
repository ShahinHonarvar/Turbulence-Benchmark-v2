def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_150 = fibonacci(149)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_150 == 0
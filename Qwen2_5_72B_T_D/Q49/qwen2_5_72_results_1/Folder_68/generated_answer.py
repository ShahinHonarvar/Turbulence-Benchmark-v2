def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_38 = fibonacci(37)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_38 == 0
def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fib_137 = fibonacci(137)
    return decimal_int % fib_137 == 0
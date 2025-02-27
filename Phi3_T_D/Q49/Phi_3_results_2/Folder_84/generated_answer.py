def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_196 = fibonacci(196)
    return decimal_int % fib_196 == 0
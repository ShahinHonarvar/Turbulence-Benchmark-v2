def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return a
    return decimal_int % fibonacci(99) == 0
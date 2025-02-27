def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return decimal_int % fibonacci(24) == 0
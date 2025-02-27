def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return n % fibonacci(198) == 0
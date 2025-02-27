def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    num = fibonacci(28)
    return decimal_val % num == 0
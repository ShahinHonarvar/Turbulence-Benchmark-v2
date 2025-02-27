def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(179):
        a, b = (b, a + b)
    fib_180 = b
    return decimal_int % fib_180 == 0
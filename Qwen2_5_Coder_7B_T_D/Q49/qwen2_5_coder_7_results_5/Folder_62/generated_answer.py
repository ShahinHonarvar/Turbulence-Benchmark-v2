def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    fib_130 = None
    for _ in range(130):
        a, b = (b, a + b)
    fib_130 = b
    decimal = int(binary_str, 2)
    return decimal % fib_130 == 0
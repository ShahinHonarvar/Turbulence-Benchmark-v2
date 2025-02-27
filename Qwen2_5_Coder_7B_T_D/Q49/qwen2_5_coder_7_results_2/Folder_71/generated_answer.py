def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(146):
        a, b = (b, a + b)
    fib_147 = b
    decimal = int(binary_str, 2)
    return decimal % fib_147 == 0
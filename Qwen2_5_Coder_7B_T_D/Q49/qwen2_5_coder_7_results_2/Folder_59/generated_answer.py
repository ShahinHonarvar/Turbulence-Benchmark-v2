def if_decimal_is_divisible(binary_str):
    fib_74 = 0
    a, b = (0, 1)
    for _ in range(74):
        a, b = (b, a + b)
    fib_74 = b
    decimal = int(binary_str, 2)
    return decimal % fib_74 == 0
def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(125):
        a, b = (b, a + b)
    fib_126 = b
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_126 == 0
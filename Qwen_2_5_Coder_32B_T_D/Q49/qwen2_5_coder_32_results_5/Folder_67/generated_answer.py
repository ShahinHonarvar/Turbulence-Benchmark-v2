def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(106):
        a, b = (b, a + b)
    fib_107 = b
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_107 == 0
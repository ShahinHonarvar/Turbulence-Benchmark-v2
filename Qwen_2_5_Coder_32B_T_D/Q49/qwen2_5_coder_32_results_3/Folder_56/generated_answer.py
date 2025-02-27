def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(83):
        a, b = (b, a + b)
    fib_84 = a
    return int(binary_str, 2) % fib_84 == 0
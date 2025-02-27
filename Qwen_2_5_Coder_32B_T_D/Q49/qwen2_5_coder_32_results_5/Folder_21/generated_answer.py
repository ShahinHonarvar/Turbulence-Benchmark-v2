def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(194):
        a, b = (b, a + b)
    return int(binary_str, 2) % a == 0
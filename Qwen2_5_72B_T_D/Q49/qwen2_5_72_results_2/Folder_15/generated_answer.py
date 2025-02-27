def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(8):
        a, b = (b, a + b)
    return decimal_value % b == 0
def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(173):
        a, b = (b, a + b)
    decimal_number = int(binary_str, 2)
    return decimal_number % a == 0
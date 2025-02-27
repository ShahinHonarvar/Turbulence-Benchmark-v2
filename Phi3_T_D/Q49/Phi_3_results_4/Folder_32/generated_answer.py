def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(178):
        a, b = (b, a + b)
    return decimal_number % a == 0
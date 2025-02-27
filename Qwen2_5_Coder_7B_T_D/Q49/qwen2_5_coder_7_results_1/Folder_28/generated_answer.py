def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(103):
        a, b = (b, a + b)
    divisor = b
    decimal_num = int(binary_str, 2)
    return decimal_num % divisor == 0
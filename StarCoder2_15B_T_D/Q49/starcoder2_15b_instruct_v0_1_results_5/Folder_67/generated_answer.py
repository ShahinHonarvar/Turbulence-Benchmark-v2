def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    a, b = (0, 1)
    for _ in range(107):
        a, b = (b, a + b)
    return decimal_integer % b == 0
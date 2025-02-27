def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    return decimal_integer % 77 == 0
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % 1937766948230474241 == 0
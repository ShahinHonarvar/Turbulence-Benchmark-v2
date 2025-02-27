def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    return decimal_number % 56 == 0
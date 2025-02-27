def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value % f125 == 0
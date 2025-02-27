def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value % 3 == 0
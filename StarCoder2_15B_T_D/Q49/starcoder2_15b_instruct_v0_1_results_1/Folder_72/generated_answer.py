def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    return decimal_int % 175 == 0
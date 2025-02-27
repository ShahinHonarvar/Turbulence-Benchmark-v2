def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 3 == 0
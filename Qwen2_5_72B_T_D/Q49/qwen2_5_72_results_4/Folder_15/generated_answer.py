def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    ninth_fibonacci = 21
    return decimal_value % ninth_fibonacci == 0
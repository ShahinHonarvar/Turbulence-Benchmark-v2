def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    if decimal_int % 126 == 0:
        return True
    else:
        return False
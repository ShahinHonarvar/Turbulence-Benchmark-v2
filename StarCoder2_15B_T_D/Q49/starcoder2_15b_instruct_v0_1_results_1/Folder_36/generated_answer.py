def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, base=2)
    if decimal_int % 150 == 0:
        return True
    else:
        return False
def if_decimal_is_divisible(binary_repr):
    decimal_int = int(binary_repr, 2)
    if decimal_int % 114 == 0:
        return True
    else:
        return False
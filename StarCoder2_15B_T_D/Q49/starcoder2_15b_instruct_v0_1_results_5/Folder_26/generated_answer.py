def if_decimal_is_divisible(decimal_str):
    decimal_int = int(decimal_str, 2)
    remainder = divmod(decimal_int, 138)[1]
    return remainder == 0
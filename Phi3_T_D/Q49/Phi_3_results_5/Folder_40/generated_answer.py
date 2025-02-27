def if_decimal_is_divisible(binary_rep: str) -> bool:
    decimal_value = int(binary_rep, 2)
    return decimal_value % 3 == 0
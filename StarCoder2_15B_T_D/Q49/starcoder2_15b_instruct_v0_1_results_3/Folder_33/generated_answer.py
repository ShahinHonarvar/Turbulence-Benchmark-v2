def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % 134 == 0:
        return True
    else:
        return False
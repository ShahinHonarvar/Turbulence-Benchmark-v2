def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % 154 == 0:
        return True
    else:
        return False
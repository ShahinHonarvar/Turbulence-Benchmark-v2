def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    if_divisible = decimal_integer % fibonacci_sequence[154] == 0
    return if_divisible
def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    first, second = (0, 1)
    for _ in range(74):
        first, second = (second, first + second)
    return decimal_number % second == 0
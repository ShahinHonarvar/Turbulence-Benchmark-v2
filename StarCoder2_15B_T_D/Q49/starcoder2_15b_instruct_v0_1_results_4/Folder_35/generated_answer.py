def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    first_number, second_number = (0, 1)
    for _ in range(187):
        first_number, second_number = (second_number, first_number + second_number)
    return decimal_integer % second_number == 0
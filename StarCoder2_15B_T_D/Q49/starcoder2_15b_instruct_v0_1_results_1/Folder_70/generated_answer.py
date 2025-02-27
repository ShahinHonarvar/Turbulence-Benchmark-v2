def if_decimal_is_divisible(binary_representation: str) -> bool:
    number = int(binary_representation, base=2)
    first_number, second_number = (0, 1)
    for _ in range(137):
        first_number, second_number = (second_number, first_number + second_number)
    return number % second_number == 0
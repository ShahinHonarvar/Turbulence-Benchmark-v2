def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    first_number, second_number = (0, 1)
    for _ in range(98):
        first_number, second_number = (second_number, first_number + second_number)
    return decimal_integer % second_number == 0
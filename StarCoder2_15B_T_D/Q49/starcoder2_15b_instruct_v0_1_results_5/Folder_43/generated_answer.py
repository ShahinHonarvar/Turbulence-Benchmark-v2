def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    first_number = 0
    second_number = 1
    for _ in range(77):
        temp = first_number
        first_number = second_number
        second_number = temp + second_number
    return decimal_integer % second_number == 0
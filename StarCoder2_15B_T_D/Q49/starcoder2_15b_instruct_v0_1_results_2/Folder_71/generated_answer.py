def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    first_number = 0
    second_number = 1
    for _ in range(146):
        temp = second_number
        second_number += first_number
        first_number = temp
    return decimal_integer % second_number == 0
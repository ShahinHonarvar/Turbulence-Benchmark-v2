def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    third_fibonacci_number = 2
    for i in range(38):
        third_fibonacci_number = third_fibonacci_number + i
    return decimal_integer % third_fibonacci_number == 0
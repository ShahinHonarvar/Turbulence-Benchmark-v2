def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    first_134_fibonacci_number = 317811
    return decimal_integer % first_134_fibonacci_number == 0
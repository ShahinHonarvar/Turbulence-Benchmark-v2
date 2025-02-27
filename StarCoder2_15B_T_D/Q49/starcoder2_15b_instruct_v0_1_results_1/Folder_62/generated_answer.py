def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    first_130_fibonacci_number = fibonacci_sequence[129]
    return decimal_integer % first_130_fibonacci_number == 0
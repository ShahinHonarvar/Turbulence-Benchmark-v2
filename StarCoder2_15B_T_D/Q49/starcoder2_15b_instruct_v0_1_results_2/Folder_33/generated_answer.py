def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    fibonacci_number = fibonacci_sequence[134]
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False
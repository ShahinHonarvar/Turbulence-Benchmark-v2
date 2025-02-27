def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    if decimal_number % 170 == 0:
        return True
    else:
        return False
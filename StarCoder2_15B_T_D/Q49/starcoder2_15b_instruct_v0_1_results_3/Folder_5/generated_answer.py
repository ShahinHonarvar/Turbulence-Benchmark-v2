def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    if decimal_number % 85 == 0:
        return True
    else:
        return False
def if_decimal_is_divisible(binary_representation_string):
    """
    Returns True if the decimal integer corresponding to the given binary representation string is divisible by 377; otherwise, returns False.
    """
    decimal_integer = int(binary_representation_string, 2)
    if decimal_integer % 377 == 0:
        return True
    return False
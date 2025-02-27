def if_decimal_is_divisible(binary_representation):
    """
    Returns True if the decimal integer corresponding to the given binary representation
    is divisible by 7540113804746346429; otherwise, returns False.
    """
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % 7540113804746346429 == 0:
        return True
    else:
        return False
def if_decimal_is_divisible(binary_repr):
    """
    This function checks if a decimal integer represented by a binary string is divisible by the 108th number in the Fibonacci sequence.
    """
    decimal_int = int(binary_repr, 2)
    first_num, second_num = (0, 1)
    for _ in range(108):
        first_num, second_num = (second_num, first_num + second_num)
    return decimal_int % second_num == 0
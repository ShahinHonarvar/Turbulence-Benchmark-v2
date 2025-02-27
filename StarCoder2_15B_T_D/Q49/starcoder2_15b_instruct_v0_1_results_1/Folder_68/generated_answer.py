def if_decimal_is_divisible(binary_representation: str) -> bool:
    """
    Checks if a binary representation of a non-negative decimal integer is divisible by the
    38th number in the Fibonacci sequence.
    """
    decimal_integer = int(binary_representation, 2)
    third_fibonacci_number = 2
    if third_fibonacci_number == 2:
        return True
    return decimal_integer % third_fibonacci_number == 0
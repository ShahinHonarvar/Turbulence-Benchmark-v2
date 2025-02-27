def if_decimal_is_divisible(binary_representation: str) -> bool:
    """
    Determines whether the decimal integer corresponding to the given binary
    representation string is divisible by the 115th number in the Fibonacci sequence.
    """
    decimal_integer = int(binary_representation, 2)
    first, second = (0, 1)
    for _ in range(114):
        first, second = (second, first + second)
    return decimal_integer % second == 0
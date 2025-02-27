def if_decimal_is_divisible(binary_representation):
    """
    The function takes a binary representation string of a non-negative decimal integer.
    The most significant digit appears first. The function returns True if the decimal
    integer corresponding to the given string is divisible by the 90th number that occurs
    in the Fibonacci sequence; otherwise, it returns False. The first number that occurs
    in the Fibonacci sequence is 0.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 91):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_integer % fibonacci_sequence[90] == 0
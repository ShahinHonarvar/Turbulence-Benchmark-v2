def if_decimal_is_divisible(binary_representation):
    """
    This is a function that takes a binary representation of a non-negative
    decimal integer as an argument and returns True if the decimal integer
    corresponding to the given string is divisible by the 60th number that
    occurs in the Fibonacci sequence; otherwise, it returns False.
    """
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 61):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_number % fibonacci_sequence[60] == 0
def if_decimal_is_divisible(binary_representation):
    """
    This function takes a binary representation of a non-negative decimal integer
    and returns True if the decimal integer corresponding to the binary representation
    is divisible by the 186th number that occurs in the Fibonacci sequence;
    otherwise, it returns False.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 187):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_integer % fibonacci_sequence[186] == 0
def if_decimal_is_divisible(binary_representation):
    """
    This function checks whether a decimal integer, represented in binary, is divisible by the 179th number in the Fibonacci sequence.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 179):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_integer % fibonacci_sequence[178] == 0
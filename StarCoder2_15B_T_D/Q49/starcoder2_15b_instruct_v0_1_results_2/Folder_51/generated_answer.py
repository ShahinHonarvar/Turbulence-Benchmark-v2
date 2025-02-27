def if_decimal_is_divisible(binary_representation: str) -> bool:
    """
    This function takes a binary representation of a non-negative decimal integer
    and checks whether the corresponding decimal integer is divisible by the 17th
    number in the Fibonacci sequence.
    """
    decimal_int = int(binary_representation, 2)
    fibonacci_sequence = [0, 1, 1]
    for i in range(3, 17):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_int % fibonacci_sequence[16] == 0
def if_decimal_is_divisible(binary_representation: str) -> bool:
    """
    Converts a binary representation of a non-negative decimal integer to decimal,
    then checks if the decimal is divisible by the 90th Fibonacci number.
    """
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    for _ in range(88):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[89] == 0
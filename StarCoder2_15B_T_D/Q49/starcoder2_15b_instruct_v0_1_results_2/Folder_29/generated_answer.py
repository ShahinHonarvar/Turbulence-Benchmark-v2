def if_decimal_is_divisible(binary_representation: str) -> bool:
    """
    Checks if the decimal integer corresponding to the given binary representation string
    is divisible by the 117th number in the Fibonacci sequence.
    """
    decimal_integer = int(binary_representation, 2)
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fibonacci_117 = (phi ** 117 - psi ** 117) / 5 ** 0.5
    return decimal_integer % fibonacci_117 == 0
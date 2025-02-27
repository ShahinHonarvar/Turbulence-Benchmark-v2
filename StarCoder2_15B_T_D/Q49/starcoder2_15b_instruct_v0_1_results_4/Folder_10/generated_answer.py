def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, base=2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_integer in fibonacci_sequence[87:89]
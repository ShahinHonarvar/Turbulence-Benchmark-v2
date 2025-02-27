def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, base=2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 84:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return decimal_integer % fibonacci_sequence[83] == 0
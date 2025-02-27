def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    index = 2
    while index < 125:
        fibonacci_sequence.append(fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2])
        index += 1
    return decimal_integer % fibonacci_sequence[124] == 0
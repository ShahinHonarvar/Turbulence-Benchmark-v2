def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_representation = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 146):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_representation % fibonacci_sequence[145] == 0
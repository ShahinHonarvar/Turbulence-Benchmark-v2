def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, base=2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 135):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_integer % fibonacci_sequence[134] == 0
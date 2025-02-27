def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal_int = int(binary_repr, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 127):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_int % fibonacci_sequence[126] == 0
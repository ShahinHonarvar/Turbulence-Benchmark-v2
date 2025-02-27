def if_decimal_is_divisible(binary_string: str) -> bool:
    decimal_int = int(binary_string, base=2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 45):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_int % fibonacci_sequence[44] == 0
def if_decimal_is_divisible(binary_string: str) -> bool:
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 176):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_integer % fibonacci_sequence[175] == 0
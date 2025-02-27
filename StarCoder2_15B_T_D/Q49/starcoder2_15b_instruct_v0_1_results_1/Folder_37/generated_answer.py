def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal_int = int(binary_repr, base=2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_int:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_int in fibonacci_sequence[46:]
def if_decimal_is_divisible(binary_representation_string: str) -> bool:
    decimal_integer = int(binary_representation_string, base=2)
    fibonacci_sequence = [0, 1]
    for _ in range(109):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return decimal_integer % fibonacci_sequence[-1] == 0
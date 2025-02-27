def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, base=2)
    fibonacci_sequence = [0, 1]
    for _ in range(23):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_int % fibonacci_sequence[24] == 0
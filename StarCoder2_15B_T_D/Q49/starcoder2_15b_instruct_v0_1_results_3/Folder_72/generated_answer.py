def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(174):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_integer % fibonacci_sequence[175] == 0
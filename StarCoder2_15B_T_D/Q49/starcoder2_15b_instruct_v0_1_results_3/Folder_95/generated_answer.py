def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 168):
        fibonacci_sequence.append(fibonacci_sequence[i - 2] + fibonacci_sequence[i - 1])
    return decimal_integer % fibonacci_sequence[167] == 0
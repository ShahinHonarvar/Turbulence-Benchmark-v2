def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    n = decimal_integer % 199
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[n] % decimal_integer == 0
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for n in range(2, 35):
        fibonacci_sequence.append(fibonacci_sequence[n - 1] + fibonacci_sequence[n - 2])
    if decimal_integer % fibonacci_sequence[33] == 0:
        return True
    else:
        return False
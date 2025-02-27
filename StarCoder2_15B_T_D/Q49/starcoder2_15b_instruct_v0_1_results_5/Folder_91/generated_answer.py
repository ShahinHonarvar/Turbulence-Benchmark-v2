def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 100):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    for i, fibonacci_number in enumerate(fibonacci_sequence):
        if i >= 6 and decimal_integer % fibonacci_number == 0:
            return True
    return False
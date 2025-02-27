def if_decimal_is_divisible(binary_representation_string):
    decimal_integer = int(binary_representation_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(173):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_integer % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
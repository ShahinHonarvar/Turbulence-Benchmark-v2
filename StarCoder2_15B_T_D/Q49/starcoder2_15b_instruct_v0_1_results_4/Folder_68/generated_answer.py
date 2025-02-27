def if_decimal_is_divisible(binary_representation_str):
    decimal_integer = int(binary_representation_str, base=2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 39):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    is_divisible = decimal_integer % fibonacci_sequence[38] == 0
    return is_divisible
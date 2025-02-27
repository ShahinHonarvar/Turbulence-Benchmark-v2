def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(47):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return decimal_int % fibonacci_sequence[-1] == 0
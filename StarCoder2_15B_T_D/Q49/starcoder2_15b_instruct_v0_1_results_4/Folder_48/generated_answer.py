def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(197):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_int % fibonacci_sequence[-1] == 0
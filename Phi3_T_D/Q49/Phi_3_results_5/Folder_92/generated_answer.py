def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci_sequence = [0, 1]
    fibonacci_7th = None
    while len(fibonacci_sequence) < 7:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    fibonacci_7th = fibonacci_sequence[-1]
    return decimal_value % fibonacci_7th == 0
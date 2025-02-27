def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_sequence[5] == 0
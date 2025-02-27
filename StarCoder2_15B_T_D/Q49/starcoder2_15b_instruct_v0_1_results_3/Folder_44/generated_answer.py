def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 159):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_int % fibonacci_sequence[158] == 0
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 88:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    divisor = fibonacci_sequence[87]
    decimal_value = int(binary_str, 2)
    return decimal_value % divisor == 0
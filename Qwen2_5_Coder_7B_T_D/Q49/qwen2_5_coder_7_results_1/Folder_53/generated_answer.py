def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for _ in range(63):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_64th = fibonacci_sequence[63]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_64th == 0
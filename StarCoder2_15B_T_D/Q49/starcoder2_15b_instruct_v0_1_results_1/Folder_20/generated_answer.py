def if_decimal_is_divisible(binary_rep):
    decimal_int = int(binary_rep, 2)
    fibonacci_sequence = [0, 1]
    i = 2
    while i <= decimal_int:
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        i += 1
    return decimal_int in fibonacci_sequence[2:]
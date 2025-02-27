def if_decimal_is_divisible(binary_rep):
    decimal_int = int(binary_rep, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 24):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_int % fibonacci_sequence[23] == 0:
        return True
    else:
        return False
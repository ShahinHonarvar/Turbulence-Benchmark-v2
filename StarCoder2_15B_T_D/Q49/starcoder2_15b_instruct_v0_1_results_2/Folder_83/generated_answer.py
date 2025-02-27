def if_decimal_is_divisible(binary_repr_str):
    decimal_int = int(binary_repr_str, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 60):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_int % fibonacci_sequence[59] == 0:
        return True
    else:
        return False
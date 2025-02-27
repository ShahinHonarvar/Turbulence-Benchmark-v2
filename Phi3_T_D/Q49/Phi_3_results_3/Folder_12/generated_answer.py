def if_decimal_is_divisible(binary_string):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 66:
        next_value = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_value)
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_seq[65] == 0
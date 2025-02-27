def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 76):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return decimal_int % fibonacci_seq[75] == 0
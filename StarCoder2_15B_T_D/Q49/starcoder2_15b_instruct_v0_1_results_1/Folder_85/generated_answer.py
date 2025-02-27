def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal_int = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 45):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    if decimal_int % fibonacci_seq[44] == 0:
        return True
    else:
        return False
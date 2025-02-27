def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_int = int(binary_representation, base=2)
    fibonacci_seq = [0, 1]
    for i in range(2, 20):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return decimal_int % fibonacci_seq[19] == 0
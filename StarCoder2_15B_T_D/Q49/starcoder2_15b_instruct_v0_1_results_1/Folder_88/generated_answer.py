def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal_int = int(binary_repr, base=2)
    fibonacci_seq = [0, 1]
    for _ in range(48):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal_int % fibonacci_seq[49] == 0
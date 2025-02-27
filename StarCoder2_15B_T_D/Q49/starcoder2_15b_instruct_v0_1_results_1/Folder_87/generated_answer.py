def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal_repr = int(binary_repr, base=2)
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] < decimal_repr:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    if fibonacci_seq[-180] == decimal_repr:
        return True
    else:
        return False
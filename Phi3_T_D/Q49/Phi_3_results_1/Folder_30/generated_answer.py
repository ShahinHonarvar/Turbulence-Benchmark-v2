def if_decimal_is_divisible(binary_str):
    if not binary_str:
        return False
    decimal_val = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 186:
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
    return decimal_val % fib_sequence[185] == 0
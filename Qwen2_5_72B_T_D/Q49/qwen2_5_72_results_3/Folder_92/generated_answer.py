def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 7:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_val % fib_sequence[6] == 0
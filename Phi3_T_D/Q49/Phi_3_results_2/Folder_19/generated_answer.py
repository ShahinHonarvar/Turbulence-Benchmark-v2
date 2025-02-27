def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 30:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if int(binary_str, 2) % fib_sequence[29] == 0:
        return True
    return False
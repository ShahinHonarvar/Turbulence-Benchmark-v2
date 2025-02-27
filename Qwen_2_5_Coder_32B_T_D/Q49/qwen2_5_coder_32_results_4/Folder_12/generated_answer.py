def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(64):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_66th = fib_sequence[65]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_66th == 0
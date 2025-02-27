def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(45):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_47th = fib_sequence[46]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_47th == 0
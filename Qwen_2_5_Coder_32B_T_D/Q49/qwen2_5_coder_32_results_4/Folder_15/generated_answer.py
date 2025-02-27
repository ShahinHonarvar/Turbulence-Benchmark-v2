def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_sequence = [0, 1]
    for _ in range(2, 9):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_value % fib_sequence[8] == 0
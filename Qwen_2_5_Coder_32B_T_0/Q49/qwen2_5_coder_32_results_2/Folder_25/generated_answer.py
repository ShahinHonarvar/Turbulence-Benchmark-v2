def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 19):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_19th = fib_sequence[18]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_19th == 0
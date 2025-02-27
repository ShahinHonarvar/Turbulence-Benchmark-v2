def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(2, 74):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_74th = fib_sequence[73]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_74th == 0
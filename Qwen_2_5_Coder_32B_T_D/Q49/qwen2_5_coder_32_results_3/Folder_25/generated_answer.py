def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(18):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_19th = fib_sequence[18]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_19th == 0
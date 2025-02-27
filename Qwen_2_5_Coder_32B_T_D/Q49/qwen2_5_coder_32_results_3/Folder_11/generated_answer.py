def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(2, 16):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    target_fib_number = fib_sequence[15]
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fib_number == 0